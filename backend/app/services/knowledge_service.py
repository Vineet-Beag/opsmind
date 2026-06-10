from app.knowledge.terraform_fixes import (
    TERRAFORM_FIXES
)


class KnowledgeService:

    @staticmethod
    def find_relevant_fixes(
        validation_error: str
    ):

        matches = []

        for item in TERRAFORM_FIXES:

            if item["error"] in validation_error:

                matches.append(
                    item["fix"]
                )

        return "\n".join(matches)
