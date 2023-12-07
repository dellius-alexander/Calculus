from fractions import Fraction

from sympy import symbols, sqrt, init_printing, pprint, cos, solve, pi, sin
from src.integral import MultipleIntegral
from src.__main__ import main

x, y, z, rho, phi, theta, r = symbols("x y z rho phi theta r")

init_printing(latex_mode="inline")

######################################################################
# Cartesian coordinates:
# --------------------------------------------------------------------
# function cartesian:
f_cart = [
    1,  # 0
]
# x interval:
x_interval_cartesian = [
    (0, 1),  # 0 # x
]
# y interval:
y_interval_cartesian = [
    (x ** 2, sqrt(x)),  # 0 # y
]
# z interval:
z_interval_cartesian = [
    (0, x+y+27),  # 0 # z
]
######################################################################
# Spherical coordinates:
# --------------------------------------------------------------------
# function spherical:
f_spher = [
    (1 / rho) * ((rho ** 2) * sin(phi)),  # 0
]
# rho interval:
rho_interval_spherical = [
    (0, 3),  # 0
]
# phi interval:
phi_interval_spherical = [
    (pi / 2, pi),  # 0
]
# theta interval:
theta_interval_spherical = [
    (0, 2 * pi),  # 0
]
######################################################################
# function cylindrical:
f_cyl = [
    r,  # 0
    r,  # 1
    r,  # 2
    (1 / sqrt(r ** 2)) * r,  # 3

]
# Cylindrical coordinates:
# rho interval:
r_interval_cyl = [
    (0, 1),  # 0
    (0, 4),  # 1
    (0, 8),  # 2
    (0, 7),  # 3
]
# theta interval:
theta_interval_cyl = [
    (0, 2 * pi),  # 0
    (0, 2 * pi),  # 1
    (0, 2 * pi),  # 2
    (0, 2 * pi),  # 3
]
# z interval:
z_interval_cyl = [
    (0, 1),  # 0
    (r ** 2, 32 - r ** 2),  # 1
    (-sqrt(8 - r ** 2), sqrt(8 - r ** 2)),  # 2
    (0, 7),  # 3
]
######################################################################
# function polar:
f_polar = [
    1 * r,  # 0
]
# Polar coordinates:
# rho interval:
r_interval_polar = [
    (0, 1),  # 0
]
# theta interval:
theta_interval_polar = [
    (0, 2 * pi),  # 0
]
######################################################################
# Selection of function and coordinates:
index = 0
systems = ["cartesian", "spherical", "cylindrical", "polar"]
sentinel = [0, 1, 2, 3]

######################################################################


def test_integrals():
    ######################################################################
    # Cartesian coordinates:
    # --------------------------------------------------------------------
    if systems[0] == "cartesian":
        print("Cartesian coordinates:")
        results = main(
            func=f_cart[index],
            var=[z, y, x],
            intervals=[z_interval_cartesian[index], y_interval_cartesian[index], x_interval_cartesian[index]],
            system="cartesian")
        assert results[-1] == Fraction(93, 10)
    # ######################################################################
    # # Spherical coordinates:
    # # --------------------------------------------------------------------
    # if systems[1] == "spherical":
    #     print("Spherical coordinates:")
    #     main(
    #         func=f_spher[index],
    #         var=[rho, phi, theta],
    #         intervals=[rho_interval_spherical[index], phi_interval_spherical[index], theta_interval_spherical[index]],
    #         system="spherical")
    # ######################################################################
    # # Cylindrical coordinates:
    # # --------------------------------------------------------------------
    # if systems[2] == "cylindrical":
    #     print("Cylindrical coordinates:")
    #     main(
    #         func=f_cyl[index],
    #         var=[r, theta, z],
    #         intervals=[r_interval_cyl[index], theta_interval_cyl[index], z_interval_cyl[index]],
    #         system="cylindrical"
    #     )
    # ######################################################################
    # # Polar coordinates:
    # # --------------------------------------------------------------------
    # if systems[3] == "polar":
    #     print("Polar coordinates:")
    #     main(
    #         func=f_polar[index],
    #         var=[r, theta],
    #         intervals=[r_interval_polar[index], theta_interval_polar[index]],
    #         system="polar"
    #     )
######################################################################
