from sympy import symbols, pprint, cos, pi, sqrt, exp, log, init_printing, solve, sin, atan, tan
from sympy.abc import theta
from src.integral import Integrate, MultipleIntegral


i, j, k, x, y, z, x0, y0, z0, a, b, c, d, dx, t, r, dr, d_theta, dy, dz = \
    symbols("i, j, k, x, y, z, x0, y0, z0, a, b, c, d, dx, t, r, dr, d_theta, dy, dz")

init_printing(latex_mode="inline")


if __name__ == "__main__":
    # function:
    f = [
        exp(5 * x + y),  # 0
        sqrt(x + 4 * y),  # 1
        y * cos(x) + 3,  # 2
        -38 * y * exp(x),  # 3
        (8 * x + 4 * y) ** 2,  # 4
        x * cos(y),  # 5
        x ** 4,  # 6
        1 * r,  # 7
        1 * r,  # 7  # 1
        1 * r,  # 7  # 2
        1 * r,  # 7  # 3
        1 * r ** 2,  # 7  # 4
        ((r*cos(theta)) * (r*sin(theta))) * r,  # 12
        sin(r ** 2) * r,  # 13
        ((2 * (r * cos(theta))) - (r * sin(theta))) * r,  # 14
        (1 * r),  # 15
        (6 * x * y),  # 16
    ]
    # x interval:
    x_interval = [
        (0, log(4)),  # 0
        (4, 9),  # 1
        (0, pi / 6),  # 2
        (0, 4),  # 3
        (y - 1, -y + 1),  # 4
        (0, 3),  # 5
        (1, exp(1)),  # 6
        (1 / sqrt(2), sqrt(cos(2 * theta))),  # 7
        (1, 2),  # 7 # 1
        (0, sin(3 * theta)),  # 7 # 2
        (1, 1 * (1 + cos(theta))),  # 7 # 3
        (4, 5),  # 7 # 4
        (0, 3),  # 12 # r
        (4, 7),  # 13 # r
        (0, 6),  # 14 # r
        (0, 2),  # 15 # r
        (0, 1),  # 16 # r
    ]
    # y interval:
    y_interval = [
        (0, log(4)),  # 0
        (0, 2),  # 1
        (5, 7),  # 2
        (x / 4, (3 * x) / 4),  # 3
        (0, 1),  # 4
        (0, x ** 2),  # 5
        (0, log(x)),  # 6
        (-pi / 6, pi / 6),  # 7
        (pi / 4, 3 * pi / 4),  # 7 # 1
        (0, pi / 2),  # 7 # 2
        (0, pi / 2),  # 7 # 3
        (pi, 2*pi),  # 7 # 4
        (0, pi/4),  # 12 # theta
        (0, 2*pi),  # 13 # theta
        (pi/4, pi/2),  # 14 # theta
        (0, 2*pi),  # 15 # theta
        (0, sqrt(x)),  # 16 # theta
    ]
    # z interval:
    z_interval = [
        (0, 10),  # 0  -> 15
        (0, 1 + x + y),  # 1  -> 16 #
    ]
    m = 16
    z_index = 1
    ######################################################################
    fxy_1 = MultipleIntegral(f[m], [z, y, x], [z_interval[z_index], y_interval[m], x_interval[m]])
    ######################################################################
