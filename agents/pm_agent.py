import json
from core.agent_base import AgentBase

PM_PROMPT = """
You are a Product Manager Agent.
Convert the brief into a structured PRD.
Output MUST be valid JSON only.
Schema:
{
  "product": "string",
  "goals": ["string"],
  "target_users": ["string"],
  "page_sections": [
      { "id": "string", "purpose": "string" }
  ]
}
"""


class PMAgent(AgentBase):
    def __init__(self):
        super().__init__("PM", PM_PROMPT)

    def process(self, brief):
        output = self.run(brief)
        return json.loads(output)
