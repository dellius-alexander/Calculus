from sympy import init_printing, symbols, Integral, pprint, \
    pretty, integrate, sqrt, cos, solve
import numpy as np
import areas as area
from numbers import Number

#####################################################################
init_printing(use_latex='true')


#####################################################################


#####################################################################
#####################################################################
#                           Net Change Theorem 1
#####################################################################
def _theorem_1(a, b, height, fa=None, fb=None, f_prime=None) -> object:
    """Net Change Theorem 1: states that the new value of a changing quantity
    equals the initial value plus the integral of the rate of change:

    - ∫ [a , b] F′(v1) dx = F(b) − F(a)
    - F(b) = F(a) + ∫ [a , b] F′(v1) dx
    - F(a) = F(b) - ∫ [a , b] F′(v1) dx
    :param a: Lower bounds
    :param b: Upper bounds
    :param height: The height of the upper bound above the v1-axis or lower bound below the v1-axis
    :param fa: F(a) - The initial change
    :param fb: F(b) - The new value of the changing quantity
    :param f_prime: F'(v1) - The integral of the rate of change
    :return: the solution or raw answer
    """
    print("\n")
    print("Net Change Theorem 2")
    if a is not None and a >= 0 and b is not None:
        base = b - a
        f_prime = 1 / 2 * base * height
        print('Lower bound: {0}\nUpper bound: {1}\nBase: {2}\nF_prime: {3}'.format(a, b, base, f_prime))
    if f_prime is None:
        fx, foa, fob, x = symbols("F'(v1), F(a), F(b), v1")
        ans = fb - fa
        sym = fob - foa
        pprint(Integral(fx, x)),
        pprint(sym)
        pprint('{0} = {1} - {2}'.format(ans, fb, fa))
    elif fa is None:
        fx, foa, fob, x = symbols("F'(v1), F(a), F(b), v1")
        ans = fb - f_prime
        sym = fob - Integral(fx, x)
        print('F(a) = \n'), pprint(sym)
        pprint('{0} = {1} - {2}'.format(ans, fb, f_prime))
    elif fb is None:
        fx, foa, fob, x = symbols("F'(v1), F(a), F(b), v1")
        ans = fa + f_prime
        sym = foa + Integral(fx, x)
        print('F(b) = \n'),
        pprint(sym)
        pprint('{0} = {1} + {2}'.format(ans, fa, f_prime))
        print("\n")
    return ans


#####################################################################
#                           Net Change Theorem 2 - 4
#####################################################################
def _theorem_2_(a, b, func, d_) -> object:
    """Net Change Theorem 1: states that the new value of a changing quantity
    equals the initial value plus the integral of the rate of change:

    - 1: Solve for the antiderivative of the integral function
    - 2: Use substitution with your lower and upper bounds to solve
            the for the net change of the given problem statement.

    - ∫ [a , b] F′(v1) dx = F(b) − F(a)
    - F(b) = F(a) + ∫ [a , b] F′(v1) dx
    - F(a) = F(b) - ∫ [a , b] F′(v1) dx
    :param a: Lower bounds
    :param b: Upper bounds
    :param func: F'(v1) : the integral function
    :param d_: the variable of integration
    :return: the solution or raw answer
    """
    print("\n")
    print("Net Change Theorem 2")
    _integral_ = Integral(func, (d_, a, b))
    _antiderivative_ = integrate(func, d_)
    ans = _antiderivative_.subs({d_: b}) - _antiderivative_.subs({d_: a})
    print("\nF'(v1) = \n\n{0}".format(pretty(_integral_)))
    print("\nF(v1) = \n\n{0}".format(pretty(_antiderivative_)))
    print("\nF(v1) = \n\n{0} - {1} = {2}".format(pretty(_antiderivative_.subs({d_: b})),
                                                pretty(_antiderivative_.subs({d_: a})), ans))
    return ans


#####################################################################
#                           Net Change Theorem 5
#####################################################################
def _theorem_5_(a, b, func, d_) -> object:
    """Net Change Theorem 5: states that the new value of a changing quantity
    equals the initial value plus the integral of the rate of change:

    - 1: Solve for the antiderivative of the integral function
    - 2: Use substitution with your lower and upper bounds to solve
            for the total range of the given problem statement.
    - 3: Solve for the variable of the function to find you v1 intercepts
            and find all values of v1 > a, your lower bounds.
            Solve for the absolute value of you new bounds:
            ∫[a , v1] & ∫[v1 , b], to find the total value of the range.
    - 4: Total Value Formula: ∫[a , b] F′(v1) dx =
            (∫[a , v1] | F(v1) − F(a) |) + (∫[a , b] | F(v1) − F(a) |)

    - ∫ [a , b] F′(v1) dx = F(b) − F(a)
    - F(b) = F(a) + ∫ [a , b] F′(v1) dx
    - F(a) = F(b) - ∫ [a , b] F′(v1) dx
    :param a: Lower bounds
    :param b: Upper bounds
    :param func: F'(v1) : the integral function
    :param d_: the variable of integration
    :return: the solution or raw answer
    """
    print("\n")
    print("Net Change Theorem 5 - Total Distance\n")
    _integral_ = Integral(func, (d_, a, b))
    _antiderivative_ = integrate(func, d_)
    ans = _antiderivative_.subs({d_: b}) - _antiderivative_.subs({d_: a})
    print("\nF'(v1) = \n\n{0}\n\n".format(pretty(_integral_)))
    print("\nF(v1) = \n\n{0}\n\n".format(pretty(_antiderivative_)))
    x_int = [k for k in solve(func) if k > a]
    x_int = x_int[0]
    print("\n\nv1 intercepts: {0}\n\nIntercepts > a: {1}".format([k for k in solve(func)], x_int))
    ans = abs(_antiderivative_.subs({d_: x_int}) - _antiderivative_.subs({d_: a})) + \
          abs(_antiderivative_.subs({d_: b}) - _antiderivative_.subs({d_: x_int}))
    print("\nF(v1) = \n\n\n| {0} - {1} | + | {2} - {3} | = {4}\n".
          format(pretty(_antiderivative_.subs({d_: x_int})), pretty(_antiderivative_.subs({d_: a})),
                 pretty(_antiderivative_.subs({d_: b})), pretty(_antiderivative_.subs({d_: x_int})), ans))
    print("\n")
    return ans

#####################################################################
#####################################################################
