import json
import os


class LearningService:

    FILE = "terraform_failures.json"

    @staticmethod
    def save(error):

        if not error:
            return

        data = []

        if os.path.exists(
            LearningService.FILE
        ):

            with open(
                LearningService.FILE,
                "r"
            ) as f:

                try:
                    data = json.load(f)
                except:
                    data = []

        data.append(error)

        with open(
            LearningService.FILE,
            "w"
        ) as f:

            json.dump(
                data,
                f,
                indent=2
            )
