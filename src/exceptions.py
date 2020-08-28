class NoStatsException(Exception):
    """
    Exception raised when user has not called capture.build_stats()
    on their captured data. Or if they did not add any data.
    """

    def __init__(self):
        self.message = (
            "Please add to the data capture and then call built_stats()"
            " before making use of `less`, `greater` and `between`"
        )
        super().__init__(self.message)
