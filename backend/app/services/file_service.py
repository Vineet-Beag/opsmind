from pathlib import Path
from datetime import datetime


class FileService:

    @staticmethod
    def save(terraform_data):

        request_id = datetime.now().strftime("%Y%m%d-%H%M%S")

        output_dir = Path(f"generated/{request_id}")

        output_dir.mkdir(parents=True, exist_ok=True)

        (output_dir / "main.tf").write_text(
            terraform_data.get("main_tf", "")
        )

        (output_dir / "variables.tf").write_text(
            terraform_data.get("variables_tf", "")
        )

        (output_dir / "outputs.tf").write_text(
            terraform_data.get("outputs_tf", "")
        )

        return str(output_dir)
