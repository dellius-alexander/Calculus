"""First let’s recall the basic facts concerning definite integrals of function of a single variable. If f(x) is
defined for a <= x <= b, we start by dividing the interval [a, b] into n sub-intervals [x_i-1, x_i] of equal width
∆x = (b-a)/n, and we choose sample points x_*i in these sub-intervals. Then we form the Riemann sum:

R = n∑i=1 f(x_*i)∆x

and take the limit of such sums as n --> ∞  to obtain the definite integral of f from a to b:

b∫a f(x) dx = lim n --> ∞ n∑i=1 f(x_*i)∆x

In the special case where f(x) > 0, the Riemann sum can be interpreted as the sum of the areas of the approximating
rectangles, and b∫a f(x) dx represents the area under the curve y = f(x) from a to b.

------------------------------------------------------------------------------------------------------------------------
Iterated Integrals:

d∫c b∫a f(x, y) dx dy = b∫a d∫c f(x, y) dy dx

If f(x, y) is defined on a rectangular region R = {(x, y) | a <= x <= b, c <= y <= d}, we can evaluate the double
integral by evaluating two single integrals. We first integrate with respect to x, treating y as a constant:

d∫c b∫a f(x, y) dx dy  = d∫c b∫a f(x, y) dx = d∫c F(x, y) |a b dy = d∫c F(b, y) - F(a, y) dy

where F(x, y) = b∫a f(x, y) dx is the indefinite integral of f(x, y) with respect to x, treating y as a constant.

Then we integrate the result with respect to y:

d∫c f(x, y) dy = d∫c f(x, y) dy = F(x, y) |c d = F(d, y) - F(c, y)

where F(x, y) = d∫c f(x, y) dy is the indefinite integral of f(x, y) with respect to y.

------------------------------------------------------------------------------------------------------------------------
Double Integrals and Limits of Integration:

If f(x, y) is defined on a rectangular region R = {(x, y) | a <= x <= b, c <= y <= d}, we divide R into n
sub-rectangles R_ij of equal width ∆x = (b-a)/n and equal height ∆y = (d-c)/m. We choose sample points (x_*ij, y_*ij)
in each sub-rectangle and form the double Riemann sum:

R = n∑i=1 m∑j=1 f(x_*ij, y_*ij)∆x∆y

and take the limit of such sums as n, m --> ∞ to obtain the double integral of f over R:

d∫c b∫a f(x, y) dx dy = lim n, m --> ∞ n∑i=1 m∑j=1 f(x_*ij, y_*ij)∆x∆y

In the special case where f(x, y) > 0, the double Riemann sum can be interpreted as the sum of the volumes of the
approximating rectangular boxes, and d∫c b∫a f(x, y) dx dy represents the volume under the surface z = f(x, y) over
the region R.

------------------------------------------------------------------------------------------------------------------------
Properties of Double Integrals:

1. ∫∫R f(x, y) dA = ∫∫R f(x, y) dx dy = d∫c b∫a f(x, y) dx dy, where R = {(x, y) | a <= x <= b, c <= y <= d}

2. ∫∫R f(x, y) dA = ∫∫R f(x, y) dx dy = b∫a d∫c f(x, y) dy dx, where R = {(x, y) | a <= x <= b, c <= y <= d}

3. ∫∫R (f(x, y) + g(x, y)) dx dy = ∫∫R f(x, y) dx dy + ∫∫R g(x, y) dx dy = d∫c b∫a f(x, y) dx dy + d∫c b∫a g(x, y) dx dy
, where R = {(x, y) | a <= x <= b, c <= y <= d}

4. ∫∫R (f(x, y) - g(x, y)) dx dy = ∫∫R f(x, y) dx dy - ∫∫R g(x, y) dx dy = d∫c b∫a f(x, y) dx dy - d∫c b∫a g(x, y) dx dy
, where R = {(x, y) | a <= x <= b, c <= y <= d}

5. ∫∫R kf(x, y) dA = k∫∫R f(x, y) dx dy = k(d∫c b∫a f(x, y) dx dy), where R = {(x, y) | a <= x <= b, c <= y <= d}
and k is a constant.

6. If f(x, y) >= 0 on R, then ∫∫R f(x, y) dA represents the volume under the surface z = f(x, y) over the region R.

7. If f(x, y) <= 0 on R, then ∫∫R f(x, y) dA represents the negative of the volume under the surface z = f(x, y) over
the region R.

8. If f(x, y) <= g(x, y) on R, then ∫∫R f(x, y) dA <= ∫∫R g(x, y) dA.

9. If f(x, y) >= 0 on R, then S ⊂ R implies ∫∫S f(x, y) dA <= ∫∫R f(x, y) dA.

10. If f(x, y) >= 0 on R, and R and S are not overlapping regions, then:
 ∫∫(R U S) f(x, y) dA  = ∫∫R f(x, y) dA + ∫∫S f(x, y) dA = ∫∫R f(x, y) dx dy + ∫∫S f(x, y) dx dy
                       = d∫c b∫a f_R(x, y) dx dy + d∫c b∫a f_S(x, y) dx dy,
                       where R and S = {(x, y) | a <= x <= b, c <= y <= d}

------------------------------------------------------------------------------------------------------------------------
Triple Integrals and Limits of Integration:

If f(x, y, z) is defined on a rectangular box B = {(x, y, z) | a <= x <= b, c <= y <= d, r <= z <= s}, we divide B into
n sub-rectangular boxes B_ijk of equal width ∆x = (b-a)/n, equal height ∆y = (d-c)/m, and equal depth ∆z = (s-r)/p.
We choose sample points (x_*ijk, y_*ijk, z_*ijk) in each sub-rectangle and form the triple Riemann sum:

R = n∑i=1 m∑j=1 p∑k=1 f(x_*ijk, y_*ijk, z_*ijk)∆x∆y∆z

and take the limit of such sums as n, m, p --> ∞ to obtain the triple integral of f over B:

s∫r d∫c b∫a f(x, y, z) dx dy dz = lim n, m, p --> ∞ n∑i=1 m∑j=1 p∑k=1 f(x_*ijk, y_*ijk, z_*ijk)∆x∆y∆z

In the special case where f(x, y, z) > 0, the triple Riemann sum can be interpreted as the sum of the volumes of the
approximating rectangular boxes, and s∫r d∫c b∫a f(x, y, z) dx dy dz represents the volume under the surface
z = f(x, y, z) over the region B.

------------------------------------------------------------------------------------------------------------------------

"""
import json
from typing import Union

from sympy import Function, Symbol, Integral, Rational, Sum, Derivative, Matrix, oo, symbols, pprint
from sympy.interactive import init_printing

init_printing(pretty_print=True)

x, y = symbols('x y')


class Integrate:
    """Class for integrating function over an interval."""
    interval: tuple
    function: Function
    variable: Symbol
    integral: Integral
    result: Union[Function, Integral, Rational, Sum, Derivative, Symbol, Matrix, list, dict]
    temp: Integral

    def __init__(self, function: Function = (x ** 2) + (y ** 2), variable: Symbol = x, interval: tuple = (0, oo)):
        """
        Class for integrating function.

        - ∫∫R f(x, y) dA = ∫∫R f(x, y) dx dy = d∫c b∫a f(x, y) dx dy, where R = {(x, y) | a <= x <= b, c <= y <= d}

        :param function: Function to be integrated, default: x^2 + y^2
        :param variable: Symbol to be integrated with respect to (default: x)
        :param interval: tuple of the form (a, b), default: (0, oo)
        """
        self.function = function
        self.variable = variable
        self.interval = interval
        self.integral = Integral(self.function, (self.variable, self.interval[0], self.interval[1]))
        self.temp = Integral(self.function, self.variable)
        self.result = self.integral.doit()

        print(f"Function: f({variable}) = ")
        pprint(self.function, wrap_line=False)
        print(f"Variable: {variable}")
        print(f"Interval: {interval[0]} <= {variable} <= {interval[1]}")
        print()
        print("Integral: ")
        pprint(self.integral, wrap_line=False)
        print()
        print("Anti-derivative: ")
        pprint(self.temp.doit(), wrap_line=False)
        print()
        print("Result: ")
        pprint(self.result, wrap_line=False)
        del self.temp

    def __dict__(self):
        return {
            "function": self.function,
            "variable": self.variable,
            "interval": self.interval,
            "integral": self.integral,
            "anti-derivative": self.integral.doit(),
            "result": self.result
        }

    def __str__(self):
        return json.dumps(
            self.__dict__(),
            default=lambda o: o.__dict__() if hasattr(o, '__dict__()') else o.__str__(),
            indent=4)


class DoubleIntegral:
    """Class for computing Double Integrals over a region R and S.

    Double Integrals and Limits of Integration:

    If f(x, y) is defined on a rectangular region R = {(x, y) | a <= x <= b, c <= y <= d}, we divide R into n
    sub-rectangles R_ij of equal width ∆x = (b-a)/n and equal height ∆y = (d-c)/m. We choose sample points (x_*ij, y_*ij)
    in each sub-rectangle and form the double Riemann sum:

    R = n∑i=1 m∑j=1 f(x_*ij, y_*ij)∆x∆y

    and take the limit of such sums as n, m --> ∞ to obtain the double integral of f over R and S:

    R = d∫c b∫a f(x, y) dx dy = lim n, m --> ∞ n∑i=1 m∑j=1 f(x_*ij, y_*ij)∆x∆y

    S = b∫a d∫c f(x, y) dy dx = lim n, m --> ∞ n∑i=1 m∑j=1 f(x_*ij, y_*ij)∆x∆y

    In the special case where f(x, y) > 0, the double Riemann sum can be interpreted as the sum of the volumes of the
    approximating rectangular boxes, and d∫c b∫a f(x, y) dx dy represents the volume under the surface z = f(x, y) over
    the region R.

    """
    intervals: [tuple]
    functions: [Function] = []
    variables: [Symbol]
    integrals: list[Integral] = []
    results: [Union[Function, Integral, Rational, Sum, Derivative, Symbol, Matrix, list, dict]] = []
    temp: [Integral] = []

    def __init__(self, function: Function = None, variables: [Symbol] = None,
                 intervals: [tuple] = None):
        """
        Class for computing Double Integrals over a region R and S.
        Args:
            function: the function to be integrated over the region R and S
            variables: the variables of integration, default: x and y
            intervals: the set of tuples of the form (a, b) for the Region R and
                          (c, d) for the Region S, default: [(0, -oo), (0, oo)]
        """
        # initialize parameters in case they are None
        if function is None:
            function = [x ** 2 + y ** 2, x ** 2 + y ** 2]
        if variables is None:
            variables = [x, y]
        if intervals is None:
            intervals = [(0, -oo), (0, oo)]
        self.functions.append(function)
        self.variables = variables
        self.intervals = intervals
        # iterate over the interval for each variable
        for i in range(len(self.variables)):
            self.integrals.append(
                Integral(
                    function,
                    (self.variables[i], self.intervals[i][0], self.intervals[i][1])
                )
            )
            self.temp.append(Integral(function, variables[i]))
            temp = self.integrals[i].doit()
            self.results.append(temp)
            function = temp
            self.functions.append(function)
        print(f"{'-' * 60}")
        print(f"Variables of integration: {variables[0]} and {variables[1]}")
        print(f"Intervals of integration:")
        pprint(f"       {intervals[0][0]} <= {variables[0]} <= {intervals[0][1]}")
        pprint(f"       {intervals[1][0]} <= {variables[1]} <= {intervals[1][1]}")
        print()
        print(f"Function: f({variables[0]}) = ")
        pprint(self.functions[0], wrap_line=False)
        print()
        print(f"Function: f({variables[1]}) = ")
        pprint(self.functions[1], wrap_line=False)
        print("\n")
        print(f"Integrations: \nfirst integrate by {variables[0]}:")
        pprint(self.integrals[0], wrap_line=False)
        print(f"then integrate by {variables[1]}:")
        pprint(self.integrals[1], wrap_line=False)
        print()
        print(f"Anti-derivative with respect to {variables[0]}:")
        pprint(self.temp[0].doit(), wrap_line=False)
        print(f"Anti-derivative with respect to  {variables[1]}:")
        pprint(self.temp[1].doit(), wrap_line=False)
        print("\n")
        print(f"Result with respect to {variables[0]}: ")
        pprint(self.results[0], wrap_line=False)
        print()
        print(f"Result with respect to {variables[1]}: ")
        pprint(self.results[1], wrap_line=False)
        print(f"{'-' * 60}")

    def __dict__(self):
        return {
            "function": self.functions,
            "variables": self.variables,
            "intervals": self.intervals,
            "integrals": self.integrals,
            "anti-derivatives": [self.integrals[0].doit(), self.integrals[1].doit()],
            "results": [self.results[0], self.results[1]]
        }

    def __str__(self):
        return json.dumps(
            self.__dict__(),
            default=lambda o: o.__dict__() if hasattr(o, '__dict__()') else o.__str__(),
            indent=4)
