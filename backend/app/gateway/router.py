from app.services.terraform_validator import TerraformValidator
from app.agents.terraform_agent import TerraformAgent
from app.services.terraform_service import TerraformService
from app.services.file_service import FileService


class AIGateway:

    @staticmethod
    def route(prompt: str):

        result = TerraformAgent.generate(prompt)

        terraform = TerraformService.parse_response(result)

        output_path = FileService.save(terraform)

        validation = TerraformValidator.validate(output_path)

        terraform["output_path"] = output_path
        terraform["validation"] = validation

        return terraform
