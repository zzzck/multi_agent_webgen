from core.message_bus import MessageBus
from agents.pm_agent import PMAgent
from agents.architect_agent import ArchitectAgent
from agents.engineer_agent import EngineerAgent


class Manager:
    def __init__(self, cp: bool = True, sp: bool = True):
        """Central coordinator for the multi-agent workflow.

        Args:
            cp: Whether agents should share full conversation history (True)
                or operate in isolation with only their current input (False).
            sp: Whether to include the Architect agent step (True) or skip it
                and connect PM output directly to the Engineer (False).
        """

        self.cp = cp
        self.sp = sp
        self.bus = MessageBus()
        self.pm = PMAgent()
        self.arch = ArchitectAgent()
        self.eng = EngineerAgent()
        self.workflow = self._build_workflow()

    def _build_workflow(self):
        steps = [
            {
                "input_topic": "brief",
                "output_topic": "prd",
                "agent": self.pm,
                "description": "Convert user brief into structured PRD",
            }
        ]

        if self.sp:
            steps.append(
                {
                    "input_topic": "prd",
                    "output_topic": "page_spec",
                    "agent": self.arch,
                    "description": "Transform PRD into page architecture",
                }
            )
            engineer_input = "page_spec"
        else:
            engineer_input = "prd"

        steps.append(
            {
                "input_topic": engineer_input,
                "output_topic": "html",
                "agent": self.eng,
                "description": "Render final HTML",
            }
        )

        return steps

    def run(self, brief, cp: bool | None = None, sp: bool | None = None):
        cp_enabled = self.cp if cp is None else cp
        sp_enabled = self.sp if sp is None else sp

        if sp_enabled != self.sp:
            # Rebuild workflow when the sp override differs from initialization
            self.sp = sp_enabled
            self.workflow = self._build_workflow()

        self.bus.publish("brief", "User", brief)

        for step in self.workflow:
            incoming = self.bus.latest(step["input_topic"])
            content = incoming["content"] if incoming else None
            context = self.bus.chat_history() if cp_enabled else []
            result = step["agent"].process(content, context=context)
            self.bus.publish(step["output_topic"], step["agent"].name, result)

        final = self.bus.latest("html")
        return final["content"] if final else ""
