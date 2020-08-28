class StatsNotBuiltError(Exception):
    """Exception raised when user has not called capture.build_stats()
      on their captured data.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self):
        self.message = (
            "Please call built_stats() before making "
            "use of `less`, `greater` and `between`"
        )
        super().__init__(self.message)
