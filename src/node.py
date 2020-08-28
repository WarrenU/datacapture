class Node():
    """
    Node keeps track of a `value`, and the `occurence` of that value
    within a master data structure. It also keeps track of the amount of
    values occuring `before` (<) and `after` (>) the `value`. Lastly,
    it keeps track of the previous node (first value less than it) and
    the next node (first value that is greater than it)
    """

    def __init__(self, value, occurence=0):
        self.value = value
        self.occurence = occurence
        self.before = 0
        self.after = 0

    def __repr__(self):
        return "<N{} #{}-{};{}>".format(
            self.value, self.occurence, self.before, self.after)
