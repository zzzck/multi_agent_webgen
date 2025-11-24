from core.agent_base import AgentBase

ENGINEER_PROMPT = """
You are a Frontend Engineer.
Generate COMPLETE HTML5 + CSS based on the page structure.
Output ONLY raw HTML code, without backticks.
"""


class EngineerAgent(AgentBase):
    def __init__(self):
        super().__init__("Engineer", ENGINEER_PROMPT)

    def process(self, page_spec):
        return self.run(str(page_spec))
