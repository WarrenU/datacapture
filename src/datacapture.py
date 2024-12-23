from src.exceptions import NoStatsException

from src.node import Node
from src.stat import Stat


class DataCapture():
    """
    DataCapture adds numbers to a list `data`, and uses that list to
    construct a `Stat` object via the `build_stats` func.
    """

    def __init__(self):
        self.data = []
        self.max_int = 0

    def add(self, x: int) -> None:
        self.data.append(x)
        if x > self.max_int:
            self.max_int = x

    def reset(self):
        self.data = []
        self.max_int = 0

    def build_stats(self) -> Stat:
        """
        build_stats will return a Stat object. The Stat object has an
        attribute called `stats` which is an array of None and Node values.
        Each index of the `stats` array is a bucket of at most 1 Node.
        For example:
            If I add in 1 and 3 into my DataCapture object...
            stats[1] will hold 1 `Node` keeping track of data for the #1
            stats[3] will hold 1 `Node` keeping track of data for the #3
            stats[0], stats[2] will be None
        """
        if self.max_int == 0:
            raise NoStatsException
        stats = [None] * (self.max_int + 1)
        total_data = len(self.data)

        # Create Node Objects per bucket in stats array.
        # Increment occurences if a number appears more than once:
        for value in self.data:
            curr = stats[value]
            if curr is None:
                stats[value] = Node(value, 1)
            else:
                curr.occurence += 1

        # Iterate over Node Objects, and determine how many numbers
        # occur after and before the given number.
        count = 0
        for v in stats:
            if v is not None:
                v.before = count
                v.after = total_data - count - v.occurence
                count += v.occurence

        return Stat(stats)
