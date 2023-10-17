from numpy import e
from sympy import symbols, pprint, cos, pi, sqrt, exp, log, init_printing
from sympy.abc import theta

from src.integral import Integrate, DoubleIntegral

i, j, k, x, y, z, x0, y0, z0, a, b, c, dx, t, r, dr, d_theta = \
    symbols("i, j, k, x, y, z, x0, y0, z0, a, b, c,  dx, t, r, dr, d_theta")

init_printing(latex_mode="inline")

if __name__ == "__main__":
    f = [
        exp(5*x+y),         # 0
        sqrt(x + 4*y),      # 1
        y * cos(x) + 3,     # 2
        -2 * y * exp(x),    # 3
        (8 * x + 4 * y) ** 2,   # 4
        x * cos(y),         # 5
        x ** 5,             # 6
        1*r                 # 7
    ]
    x_interval = [
        (0, log(4)),    # 0
        (4, 9),         # 1
        (0, pi/6),      # 2
        (0, 4),         # 3
        (y-1, -y+1),        # 4
        (0, 3),         # 5
        (1, exp(1)),    # 6
        (1/sqrt(2), sqrt(cos(2*theta)))  # 7
    ]
    y_interval = [
        (0, log(4)),    # 0
        (0, 2),         # 1
        (5, 7),         # 2
        (x/4, (3*x)/4),   # 3
        (0, 1),         # 4
        (0, x ** 2),    # 5
        (0, log(x)),    # 6
        (-pi/6, pi/6)   # 7
    ]
    n = 7
    ######################################################################
    fx = DoubleIntegral(f[n], [r, theta], [x_interval[n], y_interval[n]])

    # fy = Integrate(fx.results[0], y, y_interval[n])
    # pprint(fx.result)
    # pprint(f"{'-' * 60}")
    ######################################################################
