from sympy import symbols, init_printing, pretty_print, simplify, solve, \
    Integral, sqrt, sin, exp, ln, log, expand, Symbol, Function, \
    pretty, cos
from numbers import Number
from fractions import Fraction
import re

init_printing(use_unicode='true')


#####################################################################
#                   The Mean Value Theorem
#####################################################################
def _mean_value(fx, lower_bound, upper_bound,
                variable_of_integration, average_rate_change=None) -> object:
    """The Mean Value Theorem:

    Let f be a function such that:

    1. It is continuous on the closed interval [a, b].
    2. It is differentiable on the open interval (a, b).

    Then there is (at least) a number c in (a, b) such that

    -   f'(c) = [ f(b) - f(a) ] / [ b - a ]

    Comment: Notice that the left side is the instantaneous rate of
    change / slope of the tangent line at c, while the right side is
    the average rate of change / slope of the secant line from a to b.
    Thus the theorem guarantees that there is at least one place in (a, b)
    where the tangent line there is parallel to the secant line connecting
    the points (a, f (a)) and (b, f (b)) on the curve y = f (x).

    :param fx:
    :param lower_bound:
    :param upper_bound:
    :param variable_of_integration:
    :param average_rate_change:
    :return:
    """
    a = lower_bound
    b = upper_bound
    _var_ = variable_of_integration
    _area_ = Integral(fx, (_var_, a, b))
    avg_roc = average_rate_change
    if avg_roc is not None:
        _mean_avg_roc_ = Fraction(1 / (b - a)).limit_denominator() * avg_roc
    elif avg_roc is None:
        _mean_avg_roc_ = "None"
        _given_c = "None"
    _mean_value_theorem_of_integral_ = Fraction(1 / (b - a)).limit_denominator() * _area_.doit()
    if _mean_value_theorem_of_integral_ > 0:
        c = solve(fx - _mean_value_theorem_of_integral_)
    elif _mean_value_theorem_of_integral_ < 0:
        c = solve(fx + _mean_value_theorem_of_integral_)
    print("\nf({}) = \n".format(_var_))
    pretty_print(fx)
    print("\nIntegral: \n")
    pretty_print(_area_)
    print("\nMean value theorem for integral: \n")
    pretty_print(_mean_value_theorem_of_integral_)
    print("\nMean value given a rate of change: \n")
    pretty_print(_mean_avg_roc_)
    print("\nc from Mean value theorem for integral: \n")
    pretty_print(c)


#####################################################################
#  Fundamental Theorem of Calculus
#  #1 Derivative of an Integral Function - one & two variable
#####################################################################
def _ftc_(fx, lower_bound, upper_bound,
          variable_of_integration) -> object:
    """Fundamental Theorem of Calculus:
    #1 Derivative of an Integral Function

    Theorem: If f(x) is continuous on [a, b], then the function g defined by

    - g(x) = ∫[x, a] f(t) dt, a ≤ x ≤ b

    is continuous on [a, b] and differentiable on (a, b), and g′(x) = f(x).
    That is

    - g'(x) = d/dx ∫[x, a] f(t) dt = f(x)

    :param fx:
    :param lower_bound:
    :param upper_bound:
    :param variable_of_integration:
    :return:
    """
    a = lower_bound
    b = upper_bound
    _var_ = variable_of_integration
    regex_a = re.findall("[xy]", str(a))
    regex_b = re.findall("[xy]", str(b))
    print("\nf({}) = \n".format(_var_))
    pretty_print(fx)
    if not isinstance(a, Number) \
            and not isinstance(b, Number):
        print("\na = \n")
        pretty_print(a)
        print("\nb = \n")
        pretty_print(b)
        print("\na'({0}) = \n".format(_var_))
        if isinstance(a, Number):
            pretty_print(a)
            _variable_a = - fx.subs({_var_: a}) * a
        else:
            pretty_print(a.diff())
            _variable_a = - fx.subs({_var_: a}) * a.diff()
        print("\nb'({0}) = \n".format(_var_))
        if isinstance(b, Number):
            pretty_print(b)
            _variable_b = fx.subs({_var_: b}) * b
        else:
            pretty_print(b.diff())
            _variable_b = fx.subs({_var_: b}) * b.diff()
        _solution_ = _variable_a + _variable_b
        print("\nf(a): \n")
        pretty_print(_variable_a)
        print("\nf(b): \n")
        pretty_print(_variable_b)
        print("\nf'({})\n".format(_var_))
        pretty_print(_solution_)
    else:
        _integral_ = Integral(fx, (_var_, a, b))
        _int_sol_ = _integral_.doit()
        _derivative_of_int_sol_ = _int_sol_.diff()
        print("\nIntegral: \n")
        pretty_print(_integral_)
        print("\nIntegral Solution: \n")
        pretty_print(_int_sol_)
        print("\nDerivative of the Integral: \n")
        pretty_print(_derivative_of_int_sol_)
        print("\nSimplified: \n")
        pretty_print(expand(_derivative_of_int_sol_))

    #####################################################################
    #####################################################################
    #                           Main Method
    #####################################################################



