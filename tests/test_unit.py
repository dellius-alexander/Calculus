import re
import traceback
import unittest
from symbol import expr
from typing import Union
from src.integral import MultipleIntegral
from sympy import sin, cos, pi, sqrt, exp, oo, symbols, Integral, Matrix, Expr, Symbol, Mul, Add, Subs, Function
from sympy.abc import x, y, z, a, b, c, d, t, r, rho, theta, phi
from sympy.core import mul

from src.myLogger.logger import get_logger

log = get_logger(__name__)


class IntegrationTestCases(unittest.TestCase):
    def convert_from_cartesian_to_spherical(self):
        # actual = [(0, rho*sin(phi)*sin(theta)), (rho*sin(phi)*cos(theta), 5*rho*sin(phi)*cos(theta)), (0, 1)]
        # array = [tuple((0, y)), tuple((x, 5 * x)), tuple((0, 1))]
        actual = rho**2*sin(phi)**2*sin(theta)**2 + rho**2*sin(phi)**2*cos(theta)**2
        func = x**2 + y**2
        substitutions = {x: rho * (sin(phi)) * (cos(theta)), y: rho * (sin(phi)) * (sin(theta))}
        print('\n')
        log.debug(func)
        expected = MultipleIntegral.flatten_and_subs(func, substitutions=substitutions)
        log.debug(expected)
        self.assertEqual(actual, expected)  # add assertion here

    def test_solve_spherical(self):
        actual = 1/3 * (rho**3*sin(phi)**3)
        func = x**2 + y**2
        variables = [z, y, x]
        intervals = [(0, y), (x, 5*x), (0, 1)]
        expected = MultipleIntegral.solve_sphere(func, variables, intervals)
        self.assertEqual(actual, expected)


class SubscriptableMul:
    def __init__(self, mul_obj, substitutions=None):
        # Ensure the object is a Mul object
        if not isinstance(mul_obj, Mul):
            raise ValueError("Object must be a Mul object")

        # Convert the Mul object to a list of its components
        self.factors = list(mul_obj.args)

        # Apply substitutions if provided
        if substitutions:
            self.factors = [factor.subs(substitutions) for factor in self.factors]

    def __getitem__(self, index):
        # Make the object subscriptable
        return self.factors[index]

    def __str__(self):
        # Return the string representation of the object's dictionary
        return str(self.__dict__)


if __name__ == '__main__':
    unittest.main()
