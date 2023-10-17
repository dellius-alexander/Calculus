# Authors: Dellius Alexander
import json
from typing import List


class IPoint(object):
    """
    A point in normal^D space.
    values = [x, y, z, ...]
    """
    values: List


class Point(IPoint):
    """
    A point in normal^D space.
    values = [x, y, z, ...]
    """

    def __init__(self, *values: tuple):
        self.values = values

    def __add__(self, other: IPoint):
        return Point(*[a + b for a, b in zip(self.values, other.values)])

    def __sub__(self, other: IPoint):
        return Point(*[a - b for a, b in zip(self.values, other.values)])

    def __str__(self):
        return self.__dict__()

    def __dict__(self):
        return json.dumps(self.values, default=lambda x: x.__dict__() if hasattr(x, '__dict__') else x.__str__())
