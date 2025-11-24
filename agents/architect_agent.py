import json
from core.agent_base import AgentBase

ARCH_PROMPT = """
You are a Web Architect Agent.
Use the PRD to design a page structure.
Output STRICT JSON:
{
  "layout": "string",
  "colors": ["string"],
  "components": [
    {
      "id": "string",
      "html": "string",
      "children": [
        {
          "tag": "string",
          "content_hint": "string"
        }
      ]
    }
  ]
}
"""


class ArchitectAgent(AgentBase):
    def __init__(self):
        super().__init__("Architect", ARCH_PROMPT)

    def process(self, prd):
        output = self.run(json.dumps(prd, ensure_ascii=False))
        return json.loads(output)
