import unittest

from sympy import symbols, cos, sin
from sympy.abc import theta, r, phi, x, y, z

from src.myLogger.logger import get_logger
from subscriptable import Subscriptable

log = get_logger(__name__)


class SubscriptableMulTestCases(unittest.TestCase):
    def test_subscriptable_mul(self, func=5 * (x ** 2) + 5 * (y ** 2)):
        substitutions = {x: 1, y: 2}
        log.debug(f"""
        func: {func},
        substitutions: {substitutions}
        Type of func: {type(func)}""")
        obj = Subscriptable(func, substitutions)
        log.debug(obj)
        self.assertEqual(obj.func, func)
        self.assertEqual(obj.components[0], 5)
        self.assertEqual(obj.components[1], 20)

    def test_subscriptable_mul_with_polar_substitutions(self, func=5 * (x ** 2) + 5 * (y ** 2)):
        substitutions = {x: r * cos(theta), y: r * sin(theta)}
        log.debug(f"""
        func: {func},
        substitutions: {substitutions}
        Type of func: {type(func)}""")
        obj = Subscriptable(func, substitutions)
        log.debug(obj)
        self.assertEqual(obj.func, func)
        self.assertEqual(obj.components[0], 5 * r ** 2 * cos(theta) ** 2)
        self.assertEqual(obj.components[1], 5 * r ** 2 * sin(theta) ** 2)

    def test_subscriptable_mul_with_cylindrical_substitutions(self, func=5 * (x ** 2) + 5 * (y ** 2) - z):
        substitutions = {x: r * cos(theta), y: r * sin(theta), z: z}
        log.debug(f"""
        func: {func},
        substitutions: {substitutions}
        Type of func: {type(func)}""")
        obj = Subscriptable(func, substitutions)
        log.debug(obj)
        self.assertEqual(obj.func, func)
        self.assertEqual(obj.components[0], 5 * r ** 2 * cos(theta) ** 2)
        self.assertEqual(obj.components[1], 5 * r ** 2 * sin(theta) ** 2)
        self.assertEqual(obj.components[2], -z)

    def test_subscriptable_mul_with_spherical_substitutions(self, func=5 * (x ** 2) + 5 * (y ** 2) - z):
        substitutions = {x: r * sin(theta) * cos(phi), y: r * sin(theta) * sin(phi), z: r * cos(theta)}
        log.debug(f"""
        func: {func},
        substitutions: {substitutions}
        Type of func: {type(func)}""")
        obj = Subscriptable(func, substitutions)
        log.debug(obj)
        self.assertEqual(obj.func, func)
        self.assertEqual(obj.components[0], 5 * r ** 2 * sin(theta) ** 2 * cos(phi) ** 2)
        self.assertEqual(obj.components[1], 5 * r ** 2 * sin(theta) ** 2 * sin(phi) ** 2)
        self.assertEqual(obj.components[2], -r * cos(theta))


if __name__ == '__main__':
    unittest.main()
