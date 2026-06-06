import subprocess


class TerraformValidator:

    @staticmethod
    def validate(terraform_dir: str):

        try:

            init_result = subprocess.run(
                ["terraform", "init", "-backend=false"],
                cwd=terraform_dir,
                capture_output=True,
                text=True
            )

            validate_result = subprocess.run(
                ["terraform", "validate"],
                cwd=terraform_dir,
                capture_output=True,
                text=True
            )

            return {
                "valid": validate_result.returncode == 0,
                "init_output": init_result.stdout,
                "validation_output": validate_result.stdout,
                "validation_error": validate_result.stderr
            }

        except Exception as e:

            return {
                "valid": False,
                "error": str(e)
            }
