from sympy import init_printing, symbols, pretty, solve, pi, Integral, LC, \
    factor, sqrt, pretty_print, exp, simplify, ln, exp, log, sin, cos
from numbers import Number
from fractions import Fraction

#####################################################################
init_printing(use_unicode='true')


#####################################################################
#####################################################################
#                            Area of Square
#####################################################################
def _square_(side=Number) -> object:
    """Area = a^2
    :param side: The length of the side
    """
    print('\n')
    print('Side: {0}'.format(side))
    area = (side ** 2)
    print('Area of Square: {0}'.format(area))
    print('\n')
    return area


#####################################################################
#                            Area of Triangle
#####################################################################
def _triangle_(base, height) -> object:
    """Area = ½ * b * h
    :param base: The length of the base of the triangle
    :param height: The length of the height of the triangle
    """
    print('\n')
    print('Base: {0} \nHeight: {1}'.format(base, height))
    area = 1 / 2 * base * height
    print('Area of Triangle: {0}'.format(area))
    print('\n')
    return area


#####################################################################
#                            Area of Circle
#####################################################################
def _circle_(radius) -> object:
    """Area = π * r^2
    :param radius: The radius of the circle
    """
    print("\n")
    print('Radius: \n')
    pretty_print(radius)
    area = pi * radius ** 2
    print('\nArea of circle: \n')
    pretty_print(area)
    return area


#####################################################################
#                            Area of Rectangle
#####################################################################
def _rectangle_(length, width) -> object:
    """Area = l * w
    :param length: The length of the rectangle
    :param width: The width of the rectangle
    """
    print("\n")
    print('Length: {0}\nWidth: {1}'.format(length, width))
    area = length * width
    print('Area of rectangle: {0}'.format(area))
    print("\n")
    return area


#####################################################################
#                            Area of Parallelogram
#####################################################################
def _parallelogram_(base, height) -> object:
    """Area = b * h
    :param base: The length of the base
    :param height: The vertical length of the height
    """
    print("\n")
    print('Base: {0}\nHeight: {1}'.format(base, height))
    area = base * height
    print('Area of parallelogram: {0}'.format(area))
    print("\n")
    return area


#####################################################################
#                            Area of Trapezium
#####################################################################
def _trapezium_(a, b, height) -> object:
    """Area = 1/2 * (a + b) * h
    :param a: The length of the short parallel side
    :param b: The length of the long parallel side
    :param height: The length of the base
    """
    print("\n")
    print('Short parallel side: {0}\nLong parallel side: {1}\nHeight: {2}'.
          format(a, b, height))
    area = 1 / 2 * (a + b) * height
    print('Area of trapezium: {0}'.format(area))
    print("\n")
    return area


#####################################################################
#                            Area of Ellipse
#####################################################################
def _ellipse_(a, b) -> object:
    """Area = π * a * b
    :param a: 1/2 minor axis
    :param b: 1/2 major axis
    """
    print("\n")
    print('Minor axis: {0}\nMajor axis: {1}'.format(a, b))
    area = pi * a * b
    print('Area of ellipse: {0}'.format(area))
    print("\n")
    return area


#####################################################################
#                            Area of Cube
#####################################################################
def _cube_(a) -> object:
    """Area = 6 * a^2
    :param a: The length of the edge
    """
    print("\n")
    print('Length of the edge: {0}'.format(a))
    area = 6 * a ** 2
    print('Area of cube: {0}'.format(area))
    print("\n")
    return area


#####################################################################
#                            Area of Rectangular Prism
#####################################################################
def _rectangular_prism_(length, width, height) -> object:
    """Area = 2 * (w * l + h * l + h * w)
    :param length: The length
    :param width: The width
    :param height: The height
    """
    print("\n")
    print('Length: {0}\nWidth: {1}\nHeight: {2}'.format(length, width, height))
    area = 2 * (width * length + height * length + height * width)
    print('Area of rectangular prism: {0}'.format(area))
    print("\n")
    return area


#####################################################################
#                            Area of Cylinder
#####################################################################
def _cylinder_(radius, height) -> object:
    """Area = 2 * π * r * (r + h)
    :param radius: The redius of the circular base
    :param height: The height of the cylinder
    """
    print("\n")
    print('Radius: {0}\nHeight: {1}'.format(radius, height))
    area = 2 * pi * radius * (radius * height)
    print('Area of cylinder: {0}'.format(area))
    print("\n")
    return area


#####################################################################
#                            Area of Cone
#####################################################################
def _cone_(radius, height) -> object:
    """Area = π * r * (r + l)
    :param radius: The radius of the circular base
    :param height: The slant height
    """
    print("\n")
    print('Radius: {0}\nHeight: {1}'.format(radius, height))
    area = pi * radius * (radius + height)
    print('Area of cone: {0}'.format(area))
    print("\n")
    return area


#####################################################################
#                            Area of Sphere
#####################################################################
def _sphere_(radius) -> object:
    """Area = 4 * π * r^2
    :param radius: The radius of the sphere
    """
    print("\n")
    print('Radius: {0}'.format(radius))
    area = 4 * pi * radius ** 2
    print('Area of sphere: {0}'.format(area))
    print("\n")
    return area


#####################################################################
#                            Area of Hemisphere
#####################################################################
def _hemisphere_(radius) -> object:
    """Area = 3 * π * r^2
    :param radius: The radius of the hemisphere
    """
    print("\n")
    print('Radius: {0}'.format(radius))
    area = 3 * pi * radius ** 2
    print('Area of hemisphere: {0}'.format(area))
    print("\n")
    return area


#####################################################################
#                            Area betwen the curve 1
#####################################################################
def _bet_curve_1(fx, gx, a, b, d_) -> object:
    """Area between Curves 1: Graphs and Integrals.

    We developed the concept of the definite integral to calculate
    the area below a curve on a given interval. In this section, we
    expand that idea to calculate the area of more complex regions.
    We start by finding the area between two curves that are function
    of v1, beginning with the simple case in which one function value
    is always greater than the other. We then look at cases when the
    graphs of the function cross. Last, we consider how to calculate
    the area between two curves that are function of v2.

    Let f(v1) and g(v1) be continuous function such that f(v1) ≥ g(v1)
    or f(v1) ≤ g(v1) over an interval [a,b]. Let R denote the region
    bounded above by the graph of f(v1), below by the graph of g(v1),
    and on the left and right by the lines v1=a and v1=b, respectively.
    Therefore, on the interval [a,b], we always have f(v1) ≥ g(v1) or
    f(v1) ≤ g(v1). To determine which, we will use a test point located
    between the given interval. Solution:

    - 1: Find where f(v1) and g(v1) intersect in terms of:
            f(v1) = g(v1) and solve for v1.

    Then, the area of R is given by:

    - A = ∫[a,b] [ f(v1) − g(v1) ] dx, if f(v1) ≥ g(v1)
    - A = ∫[a,b] [ g(v1) − g(v1) ] dx, if f(v1) ≤ g(v1)

    :param fx: a function of f(v1)
    :param gx: a function of g(v1)
    :param a: The lower bounds
    :param b: The upper bounds
    :param d_: the variable of integration
    :return:  the area represented by an integral solution
                ∫[a,b] [ f(v1) − g(v1) ] dx, if f(v1) ≥ g(v1) or
                ∫[a,b] [ g(v1) − f(v1) ] dx, if f(v1) ≤ g(v1)
    """
    print("\n")
    # display f(v1)
    print('f(v1) = \n\n{0}\n\n'.format(pretty(fx)))
    # f(v1): solve for v1
    x1 = solve(fx, dict=True)
    print('f(v1):\n\nv1 = {0}\n\n'.format(x1))
    # use x1 values to get solutions of f(v1)
    for k in x1:
        y1 = fx.subs({d_: k})
        print('f({0}):\n\nv2 = {1}\n\n'.format(k, y1))
    # find the v2-intercept of f(v1)
    print('f(v1):\n\nv2-intercept = ({0}, {1})\n\n'.format(0, fx.subs({d_: 0})))
    # substitute [a, b] in f(v1)
    print('f({0}) = \n\n{1}\n\n'.format(a, fx.subs({d_: a})))
    print('f({0}) = \n\n{1}\n\n'.format(b, fx.subs({d_: b})))
    # display g(v1)
    print('g(v1) = \n\n{0}\n\n'.format(pretty(gx)))
    # g(v1): solve for v1
    x2 = solve(gx, dict=True)
    print('g(v1):\n\nv1 = {0}\n\n'.format(x2))
    # use x2 values to get solutions of g(v1)
    for k in x2:
        y2 = gx.subs({d_: k})
        print('g({0}):\n\nv2 = {1}\n\n'.format(k, y2))
    # find the v2-intercept of g(v1)
    print('g(v1):\n\nv2-intercept = ({0}, {1})\n\n'.format(0, gx.subs({d_: 0})))
    # substitute [a, b] in g(v1)
    print('g({0}) = \n\n{1}\n\n'.format(a, gx.subs({d_: a})))
    print('g({0}) = \n\n{1}\n\n'.format(b, gx.subs({d_: b})))
    # test values in the range of [a, b] to find which function is
    # hight or lower than the other in terms of the v2-axis
    for k in range(a, b):  # find which function is higher than the other
        if fx.subs({d_: k}) >= gx.subs({d_: k}):  # if f(v1) ≥ g(v1)
            sol = solve(fx - gx, dict=True)
            print('{} '.format(pretty(Integral(fx - gx))))
            print('v1 = {0}'.format(sol))
            break
        elif fx.subs({d_: k}) <= gx.subs({d_: k}):  # if f(v1) ≤ g(v1)
            sol = solve(gx - fx, dict=True)
            print('{} '.format(pretty(Integral(gx - fx))))
            print('v1 = {0}'.format(sol))
            break
    print("\n")


#####################################################################
#                            Area between the curve 2
#####################################################################
def _bet_curve_2_(fx, gx, a, b, d_) -> object:
    """Area between Curves 2: Area Bounded by Linear Functions.

    We developed the concept of the definite integral to calculate
    the area below a curve on a given interval. In this section, we
    expand that idea to calculate the area of more complex regions.
    We start by finding the area between two curves that are function
    of v1, beginning with the simple case in which one function value
    is always greater than the other. We then look at cases when the
    graphs of the function cross. Last, we consider how to calculate
    the area between two curves that are function of v2.

    Let f(v1) and g(v1) be continuous function such that f(v1) ≥ g(v1)
    or f(v1) ≤ g(v1) over an interval [a,b]. Let R denote the region
    bounded above by the graph of f(v1), below by the graph of g(v1),
    and on the left and right by the lines v1=a and v1=b, respectively.
    Therefore, on the interval [a,b], we always have f(v1) ≥ g(v1) or
    f(v1) ≤ g(v1). To determine which, we will use a test point located
    between the given interval. Solution:

    - 1: Find where f(v1) and g(v1) intersect in terms of:
            f(v1) = g(v1) and solve for v1.

    Then, the area of R is given by:

    - A = ∫[a,b] [ f(v1) − g(v1) ] dx, if f(v1) ≥ g(v1)
    - A = ∫[a,b] [ g(v1) − g(v1) ] dx, if f(v1) ≤ g(v1)

    :param fx: a function of f(v1)
    :param gx: a function of g(v1)
    :param a: The lower bounds
    :param b: The upper bounds
    :param d_: the variable of integration
    :return:  the area represented by an integral solution
                ∫[a,b] [ f(v1) − g(v1) ] dx, if f(v1) ≥ g(v1) or
                ∫[a,b] [ g(v1) − f(v1) ] dx, if f(v1) ≤ g(v1)
    """
    if not isinstance(fx, Number) and not isinstance(gx, Number):
        print("\nf(v1) & g(v1) is not number")
        f_int = Integral(fx, (d_, a, b))
        g_int = Integral(gx, (d_, a, b))
        note = ('\n***Note: The area of the region between the curves is defined as the '
                '\nintegral of the upper curve minus the integral of the lower curve over '
                '\neach region. The regions are determined by the intersection points of '
                '\nthe curves. This can be done algebraically or graphically.\n')
        if a is None and b is None:
            sol_f = solve(fx - gx)
            sol_g = solve(gx - fx)
            print('1. Combine the equations and solve for v1.  \n'
                  'f(v1) - g(v1): v1 = {0} \n\ng(v1) - f(v1): v1 = {1}'.
                  format(pretty(sol_f), pretty(sol_g)))
            if len(solve(sol_f)) <= 1 and fx.subs({d_: sol_f[0]}) >= gx.subs({d_: sol_f[0]}):
                print('Only one solution:')
                a = solve(fx)[0]
                b = sol_f[0]
        else:

            sol_f = solve(fx)
            sol_g = solve(gx)
            print('1. Solve each function for v1.  \n'
                  'f(v1): v1 = {0} \n\ng(v1): v1 = {1}'.
                  format(pretty(sol_f), pretty(sol_g)))
        # A = ∫[a,b] [ f(v1) − g(v1) ] dx, if f(v1) ≥ g(v1)
        if fx.subs({d_: a}) >= gx.subs({d_: a}):  # if f(v1) ≥ g(v1)
            print('\nf(v1) is above g(v1)\n')
            print('\n1. Eliminate the equal sides of each equation and combine '
                  '\nf(v1) = g(v1): \n\n {0} = {1} \n\n'
                  'If they f(v1) ≠ g(v1), then move to the next step.'.
                  format(pretty(fx), pretty(gx)))
            print(note)
            print('\nArea = \n\n\n{0}'.
                  format(pretty(f_int - g_int)))
            int_fg = Integral((fx - gx), (d_, a, b))
            print('\n2. Integrate to find the area between {0} and {1}'
                  '\nWe get: \n\n{2}'.format(a, b, pretty(int_fg)))
            print('3. Find the antiderivative, substitute and simplify to get: \n\n'
                  'Area between the curves = {0}'.format(pretty(int_fg.doit())))

        # A = ∫[a,b] [ g(v1) − f(v1) ] dx, if f(v1) ≤ g(v1)
        if fx.subs({d_: a}) <= gx.subs({d_: a}):  # if f(v1) ≤ g(v1)
            print('\ng(v1) is above f(v1)\n')
            fg = (gx - fx)
            print('1. Eliminate the equal sides of each equation and combine '
                  '\ng(v1) = f(v1): \n\n {0} = {1} \n\n'
                  'If they f(v1) ≠ g(v1), then move to the next step.'.
                  format(pretty(gx), pretty(fx)))
            print(note)
            print('\nArea = \n\n\n{0}'.
                  format(pretty(g_int - f_int)))
            int_fg = Integral((gx - fx), (d_, a, b))
            print('\n2. Integrate to find the area between {0} and {1}'
                  '\nWe get: \n\n{2}'.format(a, b, pretty(int_fg)))
            print('3. Find the antiderivative, substitute and simplify to get: \n\n'
                  'Area between the curves = {0}'.format(pretty(int_fg.doit())))

    elif not isinstance(fx, Number) and isinstance(gx, Number):
        print("\nOnly g(v1) is a number")
        x = symbols('v1')
        expr = Integral((fx - gx), x)
        fg = (fx - gx)
        sol = solve(fg)
        fac = factor(fg)
        _lead_coef_ = LC(fac)
        anti = expr.doit()
        note = ("***Note: If any individual factor on the left side of the \n"
                "equation is equal to 0, the entire expression will be equal to 0.***")
        print('\n\nf(v1) = \n\n{0}\n\ng(v1) = \n\n{1}\n'.format(fx, gx))
        print('\n\n1. Integrate f(v1) & g(v1) with respect to {0}: \n\n\n{1} '
              .format(d_, pretty(expr)))
        print('\n2. Comibine and rewrite as:  f(v1) = g(v1), and set equal to 0: '
              '\n\n\n{0} = 0\n'.format(pretty(fg)))
        print('\n\n3. Simplify and factor: \n\n\n{0}'.format(pretty(fac)))
        # check for and remove any leading coefficients after factoring
        print('\n\n4. Remove any leading coefficient and divide both sides of '
              'the factorials if exists by: "{0}", \nthis will cancel out the leading'
              ' coefficient leaving: \n\n{1}'.format(_lead_coef_, (fac / _lead_coef_)))
        print('\n\n5. Now solve for v1:\n{0}\n\nv1 = {1}'.
              format(note, pretty(sol)))
        print('\n\n6. The final solution is all the values that make {0} = 0 true.'
              '\nIn this case, we substitute all values of v1 = {1} found in the '
              '\nprevious step to find the coordinates where both function intersect '
              'each other.'.format(pretty(fac / _lead_coef_), sol))
        print('7. The area of the region between the curves is defined as the '
              '\nintegral of the upper curve minus the integral of the lower curve over '
              '\neach region. The regions are determined by the intersection points of '
              'the curves.')
        print('8. Now we find the antiderivative of our original integration: '
              '\n\n\n{0}\n\n\n\tOur antiderivative with respect to {1} = \n\n\n{2}\n\n'.
              format(pretty(expr), d_, pretty(anti)))
        print('\n\n8.1 Our new Integral using the antiderivative: \n\n\n{}\n\n'.
              format(pretty(Integral(anti, (x, sol[0], sol[1])))))
        print('9. Finally we substitute our intersecting points where the graphs '
              '\nintersect and subract the area under the graph from the area above '
              '\nthe graphs, to find the area between the curves, giving us: \n\n{0}'.
              format(pretty(anti.subs({d_: sol[1]})
                            - anti.subs({d_: sol[0]}))))
    elif isinstance(fx, Number) and isinstance(gx, Number):
        print("\nf(v1) & g(v1) is a number")
    elif isinstance(fx, Number) and not isinstance(gx, Number):
        print("\nOnly f(v1) is a number")


#####################################################################
#                            Area between the curve 2
#####################################################################


#####################################################################
#  Area of Compound Regions 2 - Transcendental Functions
#####################################################################
def _compound_region2_(fx, gx, lower_bound, upper_bound,
                       variable_of_integration) -> object:
    """Find The Area Bounded Above Or Below By Functions Where
    Integrating Results In A Natural Logarithmic Function:

    Let f(v1) and g(v1) be continuous function over an interval [a,b].
    Let R denote the region between the graphs of f(v1) and g(v1), and
    be bounded on the left and right by the lines v1=a and v1=b,
    respectively. Then, the area of R is given by

    - A = ∫[a, b] |f(v1)−g(v1)| dx  = A_1 + A_2

    Looking at the graph above, we can see that the area of the region
    A is comprised of two separate regions - we need to calculate the
    intersection point "v1" between the two function that falls within our
    given interval.

    We must first combine the two function to find the value of v1 where
    the two function intersect and the combined solution of f(v1) - g(v1) = 0,
    by setting f(v1) = g(v1) and simplifying, we obtain:

    - f(v1) - g(v1) = 0, if v1 is some value that makes solution 0.

    Next, we calculate |f(v1) - g(v1)| in each of the intervals [a, v1]
    and [v1, b].

    By observing the graph, if the first interval g(v1) is above f(v1) and
    the second interval f(v1) is above g(v1) we calculate the interval as:

    - A_1 = ∫ [a, v1] (g(v1) - f(v1)) dx
    - A_2 = ∫ [v1, b] (f(v1) - g(v1)) dx
    - A = A_1 + A_2, to find the area of the compound region

    Else, if the first interval f(v1) is above g(v1) and
    the second interval g(v1) is above f(v1) we calculate the interval as:

    - A_1 = ∫ [a, v1] (f(v1) - g(v1)) dx
    - A_2 = ∫ [v1, b] (g(v1) - f(v1)) dx
    - A = A_1 + A_2, to find the area of the compound region

    :param fx:
    :param gx:
    :param lower_bound:
    :param upper_bound:
    :param variable_of_integration:
    :return:
    """
    e = symbols('e')
    _a_ = lower_bound
    _b_ = upper_bound
    _f_ = fx
    _g_ = gx
    _v_ = variable_of_integration
    _sol_ = solve(fx - gx)
    print("\nIntersecting points: \n")
    [pretty_print(l) for l in _sol_]
    for k in _sol_:
        print("\nIntersecting points: \n")
        print("{0} = {1}".format(pretty((fx - gx)), pretty((fx - gx).subs({_v_: k}))))
        if (fx - gx).subs({_v_: k}) == 0 or k == 0:
            # pretty_print((fx - gx).subs({_v_: k}))
            _c_ = k
            break
        else:
            _c_ = e
            break
    if fx.subs({x: _a_}) > gx.subs({x: _a_}) and gx.subs({x: _b_}) > fx.subs({x: _b_}):
        _area_1 = Integral(fx - gx, (_v_, _a_, _c_))
        _area_1_sol_ = _area_1.doit()
        _area_2 = Integral(gx - fx, (_v_, _c_, _b_))
        _area_2_sol_ = _area_2.doit()
    else:
        _area_1 = Integral(gx - fx, (_v_, _a_, _c_))
        _area_1_sol_ = _area_1.doit()
        _area_2 = Integral(fx - gx, (_v_, _c_, _b_))
        _area_2_sol_ = _area_2.doit()
    print("\nf({}) = \n".format(_v_))
    pretty_print(fx)
    print("\ng({}) = \n".format(_v_))
    pretty_print(gx)
    print("\nIntegral Area 1 = \n".format(_v_))
    pretty_print(_area_1)
    print("\nArea 1 solution: \n")
    pretty_print(_area_1_sol_)
    print("\nIntegral Area 2 = \n".format(_v_))
    pretty_print(_area_2)
    print("\nArea 2 solution: \n")
    pretty_print(_area_2_sol_)
    print("\nArea = \n")
    pretty_print(_area_1_sol_ + _area_2_sol_)

    #####################################################################
    #####################################################################
    #                           Main Method
    #####################################################################


if __name__ == "__main__":
    # main method
    x, y, t, e = symbols('v1, v2, t, e')
    f = x**Fraction(2/3).limit_denominator()
    g = -1+x
    a = 2
    b = 3
    _variable_ = x
    # _compound_region2_(f, g, a, b, _variable_)
    pretty_print(# Fraction(_rectangle_(4, 2)).limit_denominator() + \
                 # Fraction(_triangle_(5, 5)).limit_denominator() +\
                 Fraction(_triangle_(3, 6)).limit_denominator())
