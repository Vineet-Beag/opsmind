from app.providers.gemini_provider import GeminiProvider
from app.knowledge.terraform_rules import RULES


class TerraformAgent:

    @staticmethod
    def generate(prompt: str):

        full_prompt = f"""
You are a Senior Terraform Architect.

Follow these rules strictly:

{RULES}

Return ONLY raw JSON.

Format:

{{
  "main_tf":"...",
  "variables_tf":"...",
  "outputs_tf":"..."
}}

User Request:

{prompt}
"""

        return GeminiProvider.generate(
            full_prompt
        )
