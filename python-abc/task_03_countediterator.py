#!/user/bin/python3
"""
Define class CoutedIterator that extends the built-in iterator
 obtained from the iter function


"""


class CountedIterator:
    # CountedIterator extends a standard Python
    #  iterator by keeping track of how many
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    # allowing users to monitor iteration
    # progress through the get_count() method.
    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    # allowing users to monitor iteration
    # progress through the get_count() method.
    def get_count(self):
        return self.count
