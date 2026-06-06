import json


class TerraformService:

    @staticmethod
    def parse_response(response_text: str):

        try:
            return json.loads(response_text)

        except Exception:

            return {
                "main_tf": response_text,
                "variables_tf": "",
                "outputs_tf": ""
            }
