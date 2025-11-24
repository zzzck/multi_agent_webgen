from openai import OpenAI

class AgentBase:
    def __init__(self, name, system_prompt, model="gpt-4.1"):
        self.name = name
        self.model = model
        self.system_prompt = system_prompt
        self.client = OpenAI()

    def run(self, user_prompt):
        resp = self.client.responses.create(
            model=self.model,
            input=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return resp.output_text
