import json
from typing import List

from sympy import symbols

from src.point import Point

x, y, z, x0, y0, z0, a, b, c = symbols("x, y, z, x0, y0, z0, a, b, c")


class ScalarMultipleOfPlane:
    """a(x- x0) + b(y - y0) + c(z - z0) = 0"""

    _scalar: float = 0.0
    _values: List = []
    _N: List
    _p0: List
    _p: List

    def __init__(self, normal: List = [a, b, c], p0: List = [x0, y0, z0], p: List = [x, y, z]):
        self._N: List = normal if isinstance(normal, list) else normal.values if isinstance(normal, Point) else normal
        self._p0: List = p0
        self._p: List = p
        for n, i, f in zip(self._N, self._p0, self._p):  # normal * (final - initial)
            print(f"{n}({f} - {i})")
            self._scalar += (n * (f - i))
            self._values.append(n * (f - i))

    def __str__(self):
        return json.dumps(self,
                          default=lambda x: x.__dict__() if hasattr(x, '__dict__') else x.__str__(),
                          indent=4)

    def __repr__(self):
        return self.__str__()

    def __dict__(self):
        return {
            "scalar": self._scalar,
            "values": self._values,
            "N": self._N,
            "Po": self._p0,
            "P": self._p
        }
