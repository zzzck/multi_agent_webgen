from core.message_bus import MessageBus
from agents.pm_agent import PMAgent
from agents.architect_agent import ArchitectAgent
from agents.engineer_agent import EngineerAgent


class Manager:
    def __init__(self):
        self.bus = MessageBus()
        self.pm = PMAgent()
        self.arch = ArchitectAgent()
        self.eng = EngineerAgent()

    def run(self, brief):
        self.bus.publish("brief", brief)

        prd = self.pm.process(brief)
        self.bus.publish("prd", prd)

        spec = self.arch.process(prd)
        self.bus.publish("page_spec", spec)

        html = self.eng.process(spec)
        self.bus.publish("html", html)

        return html
