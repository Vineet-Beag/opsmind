from app.providers.gemini_provider import GeminiProvider


class AutoFixAgent:

    @staticmethod
    def fix(terraform_code: dict, validation_errors: str):

        prompt = f"""
You are a Senior Terraform Architect.

IMPORTANT:
Do NOT wrap the JSON in markdown.
Do NOT use ```json.
Return ONLY raw JSON.

The following Terraform failed validation.

Fix ALL errors.

Return ONLY valid JSON.

Format:

{{
  "main_tf": "...",
  "variables_tf": "...",
  "outputs_tf": "..."
}}

Terraform:

MAIN.TF
{terraform_code.get("main_tf", "")}

VARIABLES.TF
{terraform_code.get("variables_tf", "")}

OUTPUTS.TF
{terraform_code.get("outputs_tf", "")}

Validation Errors:

{validation_errors}
"""

        return GeminiProvider.generate(prompt)
