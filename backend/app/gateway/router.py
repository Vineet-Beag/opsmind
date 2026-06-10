from app.services.terraform_validator import TerraformValidator
from app.agents.terraform_agent import TerraformAgent
from app.services.terraform_service import TerraformService
from app.services.file_service import FileService
from app.agents.autofix_agent import AutoFixAgent
from app.services.history_service import HistoryService


class AIGateway:

    @staticmethod
    def route(prompt: str):

        result = TerraformAgent.generate(prompt)

        terraform = TerraformService.parse_response(result)

        if terraform.get("error"):
            return {
                "error": terraform["error"],
                "validation": {
                    "valid": False,
                    "reason": "LLM generation failed"
                }
            }

        output_path = FileService.save(terraform)

        validation = TerraformValidator.validate(output_path)

        attempts = 1

        history = HistoryService.create()

        history = HistoryService.add(
            history,
            attempts,
            validation
        )

        max_attempts = 3

        while (
            not validation.get("valid")
            and attempts < max_attempts
        ):

            fixed_result = AutoFixAgent.fix(
                terraform,
                validation.get(
                    "validation_error",
                    ""
                )
            )

            terraform = TerraformService.parse_response(
                fixed_result
            )

            if terraform.get("error"):
                break

            output_path = FileService.save(terraform)

            validation = TerraformValidator.validate(
                output_path
            )

            attempts += 1

            history = HistoryService.add(
                history,
                attempts,
                validation
            )

        terraform["output_path"] = output_path
        terraform["validation"] = validation
        terraform["attempts"] = attempts
        terraform["history"] = history
        terraform["self_healed"] = validation.get("valid")

        return terraform
