import collections
import statistics
from collections import Counter

class Summary:
    """Computes summary statistics

    >>> s = Summary()
    >>> s.add(8)
    >>> s.add(9)
    >>> s.add(11)
    >>> round(s.mean(),2)
    9.33
    >>> s.median()
    9
    >>> print(str(s))
    mean = 9.33; median = 9
    """

    def __init__(self):
        self.counts = collections.Counter()

    def __str__(self):
        output = f'mean = {round(self.mean(),2)}; median = {round(self.median(),2)}'
        return output

    def add(self,value:int):
        self.counts[value] += 1

    def mean(self):
        return sum(key * count for key, count in self.counts.items()) / self.counts.total()

    def median(self):
        return statistics.median(self.counts.elements()) + 1


if __name__ == '__main__':
    s = Summary()
    s.add(10)
    s.add(10)
    s.add(20)
    print(str(s))