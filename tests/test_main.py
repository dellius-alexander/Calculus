import json
import unittest
from fractions import Fraction
from src.__gcd import GCD
from numpy import array, sin, cos, tan, sqrt, exp, e, sinh, cosh, tanh, arcsin, arccos, arctan, arcsinh
from sympy import Function, pi
from sympy.abc import x, y, z, r, theta, phi, rho

from src.__main__ import main
from src.myLogger.logger import get_logger
import math

log = get_logger(__name__)


class TestMain(unittest.TestCase):
    def test_main(self):
        properties = {
            "function": Function('x**2 + y**2',),
            "variables": [x, y],
            "intervals": [(0, 1), (0, 1)],
            "system": "cartesian",
        }
        log.debug(properties)
        iterated_integral = main(
            func=properties["function"],
            var=properties["variables"],
            intervals=properties["intervals"],
            system=properties["system"])
        self.assertEqual(eval(str(iterated_integral.results[-1])), eval(str(2/3)))

    def test_cartesian_to_cylindrical(self):
        properties = {
            "function": Function('x**2 + y**2', ),
            "variables": [x, y],
            "intervals": [(0, 1), (0, 1), (0, pi)],
            "system": "cyl",
        }
        log.debug(properties)
        iterated_integral = main(
            func=properties["function"],
            var=properties["variables"],
            intervals=properties["intervals"],
            system=properties["system"])
        self.assertEqual(eval(str(iterated_integral.results[-1])), eval(str(pi / 3)))

    def test_cartesian_to_spherical(self):
        properties = {
            "function": Function('rho*sin(phi)'),
            "variables": [rho, phi, theta],
            "intervals": [(0, 3), (0, pi), (0, pi)],
            "system": "sph",
        }
        log.debug(properties)
        iterated_integral = main(
            func=properties["function"],
            var=properties["variables"],
            intervals=properties["intervals"],
            system=properties["system"])
        self.assertEqual(eval(str(iterated_integral.results[-1])), eval(str(9*pi)))

    def test_cartesian_to_polar(self):
        properties = {
            "function": Function('x**2 + y**2'),
            "variables": [r, theta],
            "intervals": [(0, 1), (0, 2*pi)],
            "system": "pol",
        }
        log.debug(properties)
        iterated_integral = main(
            func=properties["function"],
            var=properties["variables"],
            intervals=properties["intervals"],
            system=properties["system"])
        self.assertEqual(eval(str(iterated_integral.results[-1])), eval(str(2*pi/3)))


if __name__ == '__main__':
    unittest.main()
