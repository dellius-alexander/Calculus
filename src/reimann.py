
import json
from typing import Callable, List, Union
from sympy import symbols, tan, sec, pprint

x, y, z = symbols("x, y, z")


class Riemann(Callable):
    """First let’s recall the basic facts concerning definite integrals of function of a single variable. If f(x) is
    defined for a <= x <= b, we start by dividing the interval [a, b] into n sub-intervals [x_i-1, x_i] of equal width
    ∆x = (b-a)/n, and we choose sample points x_*i in these sub-intervals. Then we form the Riemann sum:

    R = n∑i=1 f(x_*i)∆x

    and take the limit of such sums as n --> ∞  to obtain the definite integral of f from a to b:

    b∫a f(x) dx = lim n --> ∞ n∑i=1 f(x_*i)∆x

    In the special case where f(x) > 0, the Riemann sum can be interpreted as the sum of the areas of the approximating
    rectangles, and b∫a f(x) dx represents the area under the curve y = f(x) from a to b. """

    def __init__(self, f: Callable, a: float, b: float, n: int = 100):
        self.f = f
        self.a = a
        self.b = b
        self.n = n

        self.x = symbols("x")
        self.dx = (self.b - self.a) / self.n
        self.x_i = [self.a + i * self.dx for i in range(self.n + 1)]
        self.f_x_i = [self.f.subs(self.x, self.x_i[i]) for i in range(len(self.x_i) - 1)]
        self.R = sum(self.dx * i for i in self.f_x_i)

        self._repr = f"R = {self.R}"

    def __call__(self, *args, **kwargs):
        return self.R

    def __dict__(self):
        return json.dumps({
            "f": self.f,
            "a": self.a,
            "b": self.b,
            "n": self.n,
            "x": self.x,
            "dx": self.dx,
            "x_i": self.x_i,
            "f_x_i": self.f_x_i,
            "R": self.R
        }, default=lambda x: x.__dict__() if hasattr(x, '__dict__') else x.__str__(), indent=4)

    def __repr__(self):
        return self._repr

    def __str__(self):
        return self._repr

    def __eq__(self, other):
        return self.R == other.R

    def __ne__(self, other):
        return self.R != other.R

    def __lt__(self, other):
        return self.R < other.R

    def __le__(self, other):
        return self.R <= other.R

    def __gt__(self, other):
        return self.R > other.R

    def __ge__(self, other):
        return self.R >= other.R

    def __add__(self, other):
        return self.R + other.R

    def __sub__(self, other):
        return self.R - other.R

    def __mul__(self, other):
        return self.R * other.R

    def __truediv__(self, other):
        return self.R / other.R

    def __floordiv__(self, other):
        return self.R // other.R

    def __mod__(self, other):
        return self.R % other.R

    def __pow__(self, power, modulo=None):
        return self.R ** power


class Trapezoidal(Riemann):
    """Trapzoidal Rule"""

    def __init__(self, f: Callable, a: float, b: float, n: int = 100):
        super().__init__(f, a, b, n)
        self.R = (self.f_x_i[0] + self.f_x_i[-1] + 2 * sum(self.f_x_i[1:-1])) * self.dx / 2
        self._repr = f"R = {self.R}"

    def __dict__(self):
        return {
            "f": self.f,
            "a": self.a,
            "b": self.b,
            "n": self.n,
            "x": self.x,
            "dx": self.dx,
            "x_i": self.x_i,
            "f_x_i": self.f_x_i,
            "R": self.R
        }

    def __repr__(self):
        return self._repr

    def __str__(self):
        return self._repr


class Simpson(Riemann):
    """Simpson's Rule"""

    def __init__(self, f: Callable, a: float, b: float, n: int = 100):
        super().__init__(f, a, b, n)
        self.R = (self.f_x_i[0] + self.f_x_i[-1] + 4 * sum(self.f_x_i[1:-1:2]) + 2 * sum(self.f_x_i[2:-1:2])) * self.dx / 3
        self._repr = f"R = {self.R}"

    def __dict__(self):
        return {
            "f": self.f,
            "a": self.a,
            "b": self.b,
            "n": self.n,
            "x": self.x,
            "dx": self.dx,
            "x_i": self.x_i,
            "f_x_i": self.f_x_i,
            "R": self.R
        }

    def __repr__(self):
        return self._repr

    def __str__(self):
        return self._repr


class Midpoint(Riemann):
    """Midpoint Rule"""

    def __init__(self, f: Callable, a: float, b: float, n: int = 100):
        super().__init__(f, a, b, n)
        self.R = sum([self.f.subs(self.x, (self.x_i[i] + self.x_i[i - 1]) / 2) for i in range(self.n)]) * self.dx
        self._repr = f"R = {self.R}"

    def __dict__(self):
        return {
            "f": self.f,
            "a": self.a,
            "b": self.b,
            "n": self.n,
            "x": self.x,
            "dx": self.dx,
            "x_i": self.x_i,
            "f_x_i": self.f_x_i,
            "R": self.R
        }

    def __repr__(self):
        return self._repr

    def __str__(self):
        return self._repr


class Left(Riemann):
    """Left Riemann Sum"""

    def __init__(self, f: Callable, a: float, b: float, n: int = 100):
        super().__init__(f, a, b, n)
        self.R = sum([self.f.subs(self.x, self.x_i[i]) for i in range(self.n)]) * self.dx
        self._repr = f"R = {self.R}"

    def __dict__(self):
        return {
            "f": self.f,
            "a": self.a,
            "b": self.b,
            "n": self.n,
            "x": self.x,
            "dx": self.dx,
            "x_i": self.x_i,
            "f_x_i": self.f_x_i,
            "R": self.R
        }

    def __repr__(self):
        return self._repr

    def __str__(self):
        return self._repr


class Right(Riemann):
    """Right Riemann Sum"""

    def __init__(self, f: Callable, a: float, b: float, n: int = 100):
        super().__init__(f, a, b, n)
        self.R = sum([self.f.subs(self.x, self.x_i[i - 1]) for i in range(self.n)]) * self.dx
        self._repr = f"R = {self.R}"

    def __dict__(self):
        return {
            "f": self.f,
            "a": self.a,
            "b": self.b,
            "n": self.n,
            "x": self.x,
            "dx": self.dx,
            "x_i": self.x_i,
            "f_x_i": self.f_x_i,
            "R": self.R
        }

    def __repr__(self):
        return self._repr

    def __str__(self):
        return self._repr


if __name__ == "__main__":
    f = 16 - (x ** 2) - 2*(y ** 2)
    a = 0
    b = 2
    c = 0
    d = 2
    n = 4

    # riemann = Riemann(f, a, b, n)
    # print(riemann)
    #
    # left = Left(f, a, b, n)
    # print(left)
    #
    # right = Right(f, a, b, n)
    # print(right)
    #
    # midpoint = Midpoint(f, a, b, n)
    # print(midpoint)
    #
    # trapezoid = Trapezoidal(f, a, b, n)
    # print(trapezoid)
    #
    # simpson = Simpson(f, a, b, n)
    # print(simpson)

    riemann_sum = Riemann(f, a, b, n)
    print(riemann_sum)
    # print(riemann_sum == riemann)
    # print(riemann_sum == left)
    # print(riemann_sum == right)
    # print(riemann_sum == midpoint)
    # print(riemann_sum == trapezoid)
    # print(riemann_sum == simpson)
    print(riemann_sum.__dict__())

    print(0.5 * 0.5)


