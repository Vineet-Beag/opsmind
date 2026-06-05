from app.agents.terraform_agent import TerraformAgent


class AIGateway:

    @staticmethod
    def route(prompt: str):

        return TerraformAgent.generate(prompt)
