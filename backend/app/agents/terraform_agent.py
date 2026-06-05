from app.providers.gemini_provider import GeminiProvider


class TerraformAgent:

    @staticmethod
    def generate(user_prompt: str):

        prompt = f"""
You are a Senior Terraform Architect.

Generate production-ready Terraform code.

Requirements:
- Use OCI resources.
- Follow Terraform best practices.
- Return only Terraform code.
- No explanations.
- No markdown.

User Request:
{user_prompt}
"""

        return GeminiProvider.generate(prompt)
