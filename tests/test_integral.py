from fractions import Fraction

from sympy import symbols, sqrt, init_printing, pprint
from src.integral import MultipleIntegral


x, y, z = \
    symbols("x, y, z")

init_printing(latex_mode="inline")

# functions:
f = [
    (6 * x * y),  # 1
]
# x intervals:
x_interval = [
    (0, 1),  # 1
]
# y intervals:
y_interval = [
    (0, sqrt(x)),  # 1
]
# z intervals:
z_interval = [
    (0, 1 + x + y),  # 1
]
######################################################################


def test_integrals():
    f_index = 0
    x_index = 0
    y_index = 0
    z_index = 0
    ######################################################################
    print("\n\nf(x, y, z) = {}".format(f[f_index]))
    f_xyz = MultipleIntegral(f[f_index], [z, y, x], [z_interval[z_index], y_interval[y_index], x_interval[x_index]])
    result = f_xyz.results[-1]
    print("result = ")
    pprint(result)
    assert Fraction(f"{result}").limit_denominator(max_denominator=100) == Fraction(65/28).limit_denominator(max_denominator=100)
    ######################################################################
