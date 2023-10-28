"""First let’s recall the basic facts concerning definite integrals of function of a single variable. If f(x) is
defined for a <= x <= b, we start by dividing the interval [a, b] into fxyz sub-intervals [x_i-1, x_i] of equal width
∆x = (b-a)/fxyz, and we choose sample points x_*i in these sub-intervals. Then we form the Riemann sum:

R = fxyz∑i=1 f(x_*i)∆x

and take the limit of such sums as fxyz --> ∞  to obtain the definite integral of f from a to b:

b∫a f(x) dx = lim fxyz --> ∞ fxyz∑i=1 f(x_*i)∆x

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

If f(x, y) is defined on a rectangular region R = {(x, y) | a <= x <= b, c <= y <= d}, we divide R into fxyz
sub-rectangles R_ij of equal width ∆x = (b-a)/fxyz and equal height ∆y = (d-c)/m. We choose sample points (x_*ij, y_*ij)
in each sub-rectangle and form the double Riemann sum:

R = fxyz∑i=1 m∑j=1 f(x_*ij, y_*ij)∆x∆y

and take the limit of such sums as fxyz, m --> ∞ to obtain the double integral of f over R:

d∫c b∫a f(x, y) dx dy = lim fxyz, m --> ∞ fxyz∑i=1 m∑j=1 f(x_*ij, y_*ij)∆x∆y

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
fxyz sub-rectangular boxes B_ijk of equal width ∆x = (b-a)/fxyz, equal height ∆y = (d-c)/m, and equal depth ∆z = (s-r)/p.
We choose sample points (x_*ijk, y_*ijk, z_*ijk) in each sub-rectangle and form the triple Riemann sum:

R = fxyz∑i=1 m∑j=1 p∑k=1 f(x_*ijk, y_*ijk, z_*ijk)∆x∆y∆z

and take the limit of such sums as fxyz, m, p --> ∞ to obtain the triple integral of f over B:

s∫r d∫c b∫a f(x, y, z) dx dy dz = lim fxyz, m, p --> ∞ fxyz∑i=1 m∑j=1 p∑k=1 f(x_*ijk, y_*ijk, z_*ijk)∆x∆y∆z

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
    anti_derivative: Integral

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
        self.anti_derivative = Integral(self.function, self.variable)
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
        pprint(self.anti_derivative.doit(), wrap_line=False)
        print()
        print("Result: ")
        pprint(self.result, wrap_line=False)

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


class MultipleIntegral:
    intervals: [tuple]
    functions: [Function] = []
    variables: [Symbol] = []
    integrals: [Integral] = []
    results: [Union[Function, Integral, Rational, Sum, Derivative, Symbol, Matrix, list, dict]] = []
    anti_derivatives: [Integral] = []
    _type: str = ""

    def __init__(self, func: Function = None, variables=None, intervals: [tuple] = None, **kwargs):
        """Class for computing Double/Multiple Integrals over a region R.

        Iterated Integrals and Limits of Integration:

        - Let f: f(x,y,...,n) -> R^N , where n is in the set of variables defined on a region
        R = {(x,y,...,N_n) | a_1 <= x <= b_1, a_2 <= y <= b_2, ..., a_n <= N_n <= b_n}.

        If f(x_1, x_2, ..., x_n) is defined on a rectangular region R = {(x_1, x_2, ..., x_n) | a_1 <= x_1 <= b_1,
        a_2 <= x_2 <= b_2, ..., a_n <= x_n <= b_n}, we divide R into fxyz sub-rectangles R_i1i2...in of equal width
        ∆x_1 = (b_1-a_1)/fxyz, equal height ∆x_2 = (b_2-a_2)/m, ..., and equal depth ∆x_n = (b_n-a_n)/n. We choose sample
        points (x_*i1i2...in) in each sub-rectangle and form the n-fold Riemann sum:

        - R = fxyz∑i1=1 m∑i2=1 ... n∑in=1 f(x_*i1i2...in)∆x_1∆x_2...∆x_n

        and take the limit of such sums as fxyz, m, n --> ∞ to obtain the n-fold integral of f over R:

        - R = b_n∫a_n ... b_2∫a_2 b_1∫a_1 f(x_1, x_2, ..., x_n) dx_1 dx_2 ... dx_n = lim fxyz, m, n --> ∞
            fxyz∑i1=1 m∑i2=1 ... n∑in=1 f(x_*i1i2...in)∆x_1∆x_2...∆x_n

        In the special case where f(x_1, x_2, ..., x_n) > 0, the n-fold Riemann sum can be interpreted as the sum of the
        volumes of the approximating rectangular boxes, and b_n∫a_n ... b_2∫a_2 b_1∫a_1 f(x_1, x_2, ..., x_n) dx_1 dx_2 ... dx_n
        represents the volume under the surface z = f(x_1, x_2, ..., x_n) over the region R.

        --------------------------------------------------------------------------------------------------------------------

        Args:
            func: the function to be integrated over the region R and S
            variables: [Symbol] the variables of integration, default: x and y
            intervals: the set of tuples of the form (a, b) for the Region R and
                            (c, d) for the Region S, default: [(0, -oo), (0, oo)]
            **kwargs: type: the type of integral to be computed, default: double,

                        method: the method of integration to be used, default: riemann_sum
                        show_steps: whether to show the steps of the computation, default: False
                        depth: the depth of the recursion, default: 0
                        max_depth: the maximum depth of the recursion, default: 100
                        max_steps: the maximum number of steps to be taken, default: 1000
                        max_time: the maximum time to be taken, default: 10
                        max_error: the maximum error to be tolerated, default: 0.001
                        max_precision: the maximum precision to be used, default: 100
                        max_terms: the maximum number of terms to be used in a series, default: 100

        """
        # initialize parameters in case they are None
        if variables is None:
            variables = [x, y]
        if func is None:
            func = [x ** 2 + y ** 2, x ** 2 + y ** 2]
        if variables is None:
            variables = [x, y]
        if intervals is None:
            intervals = [(0, -oo), (0, oo)]
        self.integrate(func, variables, intervals, **kwargs)
        self.print_data()

    def __dict__(self):
        return {
            "function": self.functions,
            "variables": self.variables,
            "intervals": self.intervals,
            "integrals": self.integrals,
            "anti-derivatives": [a.doit() for a in self.anti_derivatives],
            "results": [self.results[0], self.results[1]]
        }

    def __str__(self):
        return json.dumps(
            self.__dict__(),
            default=lambda o: o.__dict__() if hasattr(o, '__dict__()') else o.__str__(),
            indent=4)

    def integrate(self, func: Function = None, variables: [Symbol] = None,
                  intervals: [tuple] = None, **kwargs):
        # initialize parameters in case they are None
        if func is None:
            func = [x ** 2 + y ** 2, x ** 2 + y ** 2]
        if variables is None:
            variables = [x, y]
        if intervals is None:
            intervals = [(0, -oo), (0, oo)]
        self._type = kwargs.get("type", "double")
        self.functions.append(func)
        self.variables = variables
        self.intervals = intervals
        _temp = []
        # iterate over the interval for each variable
        for i in range(len(self.variables)):
            self.integrals.append(
                Integral(
                    func,
                    (self.variables[i], self.intervals[i][0], self.intervals[i][1])
                )
            )
            temp = self.integrals[i].doit()
            self.results.append(temp)
            _temp.append(Integral(func, variables[i]))
            func = temp
            self.functions.append(func)
        self.anti_derivatives = _temp
        return self.results[-1]

    def print_data(self):
        """
        Prints the data for all integrals
        """
        print(f"{'-' * 70}")
        print("Variables of integration Order: ", end="")
        for i in range(len(self.variables)):
            if i < len(self.variables) - 1:
                print(f"{self.variables[i]}, ", end="")
            else:
                print(f"{self.variables[i]}")
        print("Intervals of integration:")
        for i in range(len(self.intervals)):
            print(f"       {self.intervals[i][0]} <= {self.variables[i]} <= {self.intervals[i][1]}")
        for i in range(len(self.variables)):
            print("\nFunction: f(", end="")
            print(f"{self.variables[i]}", end="")
            print(") = \n")
            pprint(self.functions[i], wrap_line=False)
        for i in range(len(self.variables)):
            print(f"\n\nIntegral with respect to {self.variables[i]}:  {self.intervals[i][0]} ∫ {self.intervals[i][1]} "
                  f"f({self.variables[i]}) =\n")
            pprint(self.integrals[i], wrap_line=False)
        for i in range(len(self.variables)):
            print(f"\n\nAnti-derivative with respect to {self.variables[i]}: F'({self.variables[i]}) =\n")
            pprint(self.anti_derivatives[i].doit(), wrap_line=False)
        for i in range(len(self.variables)):
            print(f"\n\nResult with respect to {self.variables[i]}: \n")
            pprint(self.results[i], wrap_line=False)
        print(f"{'-' * 70}")
