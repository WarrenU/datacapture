from src.exceptions import StatsNotBuiltError


class Stat():
    def __init__(self, stats):
        self.stats = stats

    def less(self, x: int) -> int:
        self.validate_stats_built()
        return self.stats[x].before

    def greater(self, x: int) -> int:
        self.validate_stats_built()
        return self.stats[x].after

    def between(self, lower: int, upper: int) -> int:
        """
        between returns a count of numbers that occur within the stats
        datastructure (list of Node). This range is inclusive.
        """
        self.validate_stats_built()
        lo = self.stats[lower]
        up = self.stats[upper]
        return lo.occurence + lo.after - up.after

    def validate_stats_built(self):
        """
        validate_stats_built will raise a StatsNotBuiltError if a user
        tries to call `less`, `greater` or `between` before calling
        build_stats()
        """
        if self.stats is None:
            raise StatsNotBuiltError
