class HistoryService:

    @staticmethod
    def create():

        return []

    @staticmethod
    def add(
        history,
        attempt,
        validation
    ):

        history.append(
            {
                "attempt": attempt,
                "valid": validation.get(
                    "valid"
                ),
                "error": validation.get(
                    "validation_error",
                    ""
                )
            }
        )

        return history
