from app.providers.gemini_provider import GeminiProvider


class TerraformAgent:

    @staticmethod
    def generate(user_prompt: str):

        prompt = f"""
You are a Senior Terraform Architect.

Generate Terraform for Oracle Cloud Infrastructure (OCI).

Return ONLY valid JSON.

Format:

{{
  "main_tf": "terraform code",
  "variables_tf": "terraform variables",
  "outputs_tf": "terraform outputs"
}}

No markdown.
No explanation.
No code fences.

User Request:
{user_prompt}
"""

        return GeminiProvider.generate(prompt)
