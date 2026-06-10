from app.providers.gemini_provider import GeminiProvider
from app.knowledge.terraform_rules import RULES


class AutoFixAgent:

    @staticmethod
    def fix(terraform_code, validation_errors):

        prompt = f"""
You are a Senior Terraform Architect.

Follow these rules:

{RULES}

Terraform failed validation.

Fix every issue.

Return ONLY raw JSON.

Format:

{{
  "main_tf":"...",
  "variables_tf":"...",
  "outputs_tf":"..."
}}

MAIN.TF

{terraform_code.get("main_tf","")}

VARIABLES.TF

{terraform_code.get("variables_tf","")}

OUTPUTS.TF

{terraform_code.get("outputs_tf","")}

VALIDATION ERRORS

{validation_errors}
"""

        return GeminiProvider.generate(prompt)
