import unittest
from fractions import Fraction

from sympy.abc import x, y, z, r, theta, phi
from sympy import cos, sin

from integral import MultipleIntegral
from subscriptable import Subscriptable
from src.myLogger.logger import get_logger

log = get_logger(__name__)


class TestConstructIntegral(unittest.TestCase):

    def test_construct_integral(self):
        func = 5 * (x ** 2) + 5 * (y ** 2)
        variables = [y, x]
        intervals = [(x ** 2, x), (0, 1),]
        integral, states = MultipleIntegral.construct_integral(func, variables, intervals)
        log.debug(f"""
        func: {func}
        variables: {variables}
        intervals: {intervals}
        integral: {integral.__str__()}
        states: {states}
        """)
        self.assertEqual(eval(str(states['anti_derivatives'][-1])), eval(str(3/7)))


if __name__ == '__main__':
    unittest.main()