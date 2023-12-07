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
integral by evaluating two single integrals. We first _integrate with respect to x, treating y as a constant:

d∫c b∫a f(x, y) dx dy  = d∫c b∫a f(x, y) dx = d∫c F(x, y) |a b dy = d∫c F(b, y) - F(a, y) dy

where F(x, y) = b∫a f(x, y) dx is the indefinite integral of f(x, y) with respect to x, treating y as a constant.

Then we _integrate the result with respect to y:

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
import re
import traceback
from dataclasses import dataclass, field
from typing import Union, List, Tuple
from sympy import Function, Symbol, Integral, Rational, Sum, Derivative, Matrix, oo, symbols, pprint, \
    cos, sin, atan, sqrt, Mul, Add, Subs, Basic, Expr, pi
from sympy.codegen.ast import String
from sympy.core.function import UndefinedFunction
from sympy.core.numbers import Zero, Number
from sympy.interactive import init_printing
from sympy.abc import phi, theta, rho, x, y, z, r
import numpy as np
from myLogger.logger import get_logger
from subscriptable import Subscriptable

init_printing(pretty_print=True)

log = get_logger(__name__)


@dataclass
class Integrate:
    """Class for integrating function over an interval."""
    integral: Integral
    solution: Union[Function, Integral, Rational, Sum, Derivative, Symbol, Matrix, list, dict]
    _type: str
    intervals: list = field(default_factory=list)
    functions: list = field(default_factory=list)
    variables: list = field(default_factory=list)
    integrals: list = field(default_factory=list)
    results: List[Union[Function, Integral, Rational, Sum, Derivative, Symbol, Matrix, list, dict]] = field(
        default_factory=list)
    anti_derivatives: List = field(default_factory=list)

    states: dict = field(
        default_factory=lambda: {'integrals': [], 'anti_derivatives': []})

    def _integrate(self, func: Function = None, variables: [Symbol] = None,
                   intervals: [tuple] = None, **kwargs):
        """
        Recursively integrates the function over the interval
        Args:
            func: the function to be integrated
            variables: the variables of integration
            intervals: the intervals of integration
            **kwargs: sentinel: the sentinel to stop the recursion

        Returns: the result of the integral(s)

        """
        try:
            # create a sentinel to stop the recursion at depth 5
            # initialize parameters in case they are None
            if func is None:
                func = [x ** 2 + y ** 2, x ** 2 + y ** 2]
            if variables is None:
                variables = [x, y]
            if intervals is None:
                intervals = [(0, -oo), (0, oo)]
            self.functions = [func]
            self._type = kwargs.get("type", "double")
            self.variables = variables
            self.intervals = intervals
            # iterate over the interval for each variable
            self.integral, self.states = MultipleIntegral.construct_integral(func, variables, intervals)
            self.anti_derivatives = self.states["anti_derivatives"]
            self.solution = self.states["anti_derivatives"][-1]
            self.integrals = self.states["integrals"]
            self.results = np.array(self.solution, dtype=object).flatten().tolist()
            # create recursive json object
            log.debug(self.__str__())

            return self.solution
        except Exception as e:
            log.error(e)
            traceback.print_exc()
            raise e

    @staticmethod
    def plot(self, **kwargs):
        """
        Plots the functions and integrals
        """
        # TODO: add support for plotting multiple integrals onto 2D and 3D graphs. To be completed by 2023-12-31
        pass

    @staticmethod
    def remove_duplicates(array: Union[List, Tuple, np.ndarray]):
        """
        Removes duplicates from an array
        Args:
            array: the array to be processed, can be multidimensional array. If multidimensional, the array will be
            flattened and then processed.

        Returns: the array with duplicates removed

        """
        array_to_set = set()
        try:
            math_regex = re.compile(
                r"^(<class 'sympy.core.mul.Mul'>|<class 'sympy.core.add.Add'>|<class 'sympy.core.numbers.Integer'>|"
                r"<class 'sympy.integrals.integrals.Integral'>|Integral|Function|Symbol|Derivative|str)$",
                re.IGNORECASE)
            deep_array_regex = re.compile(
                r"^(<class 'numpy.ndarray'>|numpy.ndarray|<class 'list'>|<class 'tuple'>)$",
                re.IGNORECASE)

            log.debug("Type of input array: %s | %s | %s ", type(array[0]), type(array),
                      math_regex.search(str(type(array[0]))))

            # Remove duplicate functions
            if math_regex.search(str(type(array[0]))):
                log.debug(f"Type of array: {type(array)}")
                log.debug(f"Array: {array}")
                array_to_set.update(array)
                log.debug(f"Array to Set: {array_to_set}")
            elif deep_array_regex.search(str(type(array[0]))):
                log.debug(f"Type of array: {type(array)}")
                log.debug(f"Array: {array}")
                # Use Numpy to flatten the array
                array_to_set.update(np.array(array).flatten().tolist())
                log.debug(f"Array to Set: {array_to_set}")
            else:
                raise TypeError(f"Type of array: {type(array)} is not supported")
            return [a for a in array_to_set]
        except Exception as e:
            log.error(e)
            traceback.print_exc()
            raise e

    @staticmethod
    def cartesian_to_spherical(x, y, z):
        rho = sqrt(x ** 2 + y ** 2 + z ** 2)
        theta = atan(y / x)
        phi = atan(sqrt(x ** 2 + y ** 2) / z)
        return rho, theta, phi

    @staticmethod
    def spherical_to_cartesian(rho, theta, phi):
        x = rho * sin(phi) * cos(theta)
        y = rho * sin(phi) * sin(theta)
        z = rho * cos(phi)
        return x, y, z

    @staticmethod
    def cartesian_to_cylindrical(x, y, z):
        r = sqrt(x ** 2 + y ** 2)
        theta = atan(y / x)
        return r, theta, z

    @staticmethod
    def cylindrical_to_cartesian(r, theta, z):
        x = r * cos(theta)
        y = r * sin(theta)
        return x, y, z

    @staticmethod
    def polar_to_cartesian(r, theta):
        x = r * cos(theta)
        y = r * sin(theta)
        return x, y

    @staticmethod
    def cartesian_to_polar(x, y):
        r = sqrt(x ** 2 + y ** 2)
        theta = atan(y / x)
        return r, theta

    @staticmethod
    def custom_subs(expr, substitutions):
        # If expr is not a SymPy expression, return it as it is
        if not isinstance(expr, Basic):
            expr = eval(str(expr))
        log.debug(f"""\n
        Function: {expr}\n
        Substitutions: {substitutions}\n""")
        # If expr is a SymPy expression, substitute each variable with its corresponding value
        for var, value in substitutions.items():
            log.debug(f"""\n
            Function: {expr}\n
            Variable: {var}\n
            Value: {value}\n""")
            expr = expr.subs(var, value)
        log.debug(f"""
        Function: {expr}\n
        Substitutions: {substitutions}\n""")
        return expr

    @staticmethod
    def process_list(matrix, substitutions):
        try:
            if isinstance(matrix[0], list):
                return [MultipleIntegral.flatten_and_subs(item, substitutions) for item in Matrix(matrix).tolist()]
            elif isinstance(matrix[-1], tuple):
                return [MultipleIntegral.flatten_and_subs(item, substitutions) for item in matrix]
            else:
                return [MultipleIntegral.flatten_and_subs(item, substitutions) for item in matrix]
        except Exception as e:
            print(e)
            traceback.print_exc()
            raise e

    @staticmethod
    def process_undefined_function(_function: Union[object, str, Function, UndefinedFunction], substitutions):
        try:
            vars_found = re.compile(r"([a-zA-Z]+)").findall(str(_function))
            substitutions = {Symbol(var): substitutions.get(Symbol(var)) for var in vars_found}
            log.debug("\n%s\n%s", type(_function), _function)
            _function = _function.subs(vars_found, substitutions.values())
            log.debug(f"""
            Function: {_function}\n
            Substitutions: {substitutions}\n""")
            return _function
        except Exception as e:
            print(e)
            traceback.print_exc()
            raise e

    @staticmethod
    def flatten_and_subs(matrix: Union[tuple, list, list[list], list[tuple], object, symbols, Integral, Matrix],
                         substitutions=None) -> list or tuple:
        """Flattens a matrix and substitutes the variables with the substitutions provided.

        Args:
            matrix (Union[tuple, list, list[list], list[tuple], object, symbols, Integral, Matrix]):
                The matrix to be flattened and substituted.
            substitutions ([type], optional): [description]. Defaults to None.

        Returns:
            object: The flattened and substituted matrix.
            """
        try:
            log.debug("\n%s\n%s", type(matrix), matrix)
            if substitutions is None:
                raise ValueError("substitutions cannot be None")
            if isinstance(matrix, (int, float, Zero, Number)):
                log.debug(f"""\nFunction: {matrix}\nSubstitutions: {substitutions}\n""")
                return matrix
            elif isinstance(matrix, list):
                log.debug(f"""\nFunction: {matrix}\nSubstitutions: {substitutions}\n""")
                return MultipleIntegral.process_list(matrix, substitutions)
            elif isinstance(matrix, tuple):
                log.debug(f"""\nFunction: {matrix}\nSubstitutions: {substitutions}\n""")
                return tuple(MultipleIntegral.flatten_and_subs(item, substitutions) for item in matrix)
            elif isinstance(matrix, Basic):  # Check if matrix is a SymPy expression
                log.debug(f"""\nFunction: {matrix}\nSubstitutions: {substitutions}\n""")
                return matrix.subs(substitutions) if isinstance(substitutions, dict) else matrix
            elif isinstance(matrix, UndefinedFunction):
                log.debug(f"""\nFunction: {matrix}\nSubstitutions: {substitutions}\n""")
                return MultipleIntegral.process_undefined_function(matrix, substitutions)
            else:
                raise TypeError(f"Type: {type(matrix)} is not supported")
        except Exception as e:
            print(e)
            traceback.print_exc()
            raise e  # re-raise the exception to the caller

    @staticmethod
    def solve_cylindrical(func: Function, variables: Union[list, tuple], intervals: Union[List[List], Tuple[Tuple]]):
        """
        In the cylindrical coordinate system, the Cartesian coordinates (x, y, z) correspond to the cylindrical coordinates (rho, theta, z) as follows:
rho: This is the radial distance from the origin (0,0) in the xy-plane. It corresponds to the distance from the z-axis to the point in the xy-plane, which is equivalent to sqrt(x^2 + y^2) in Cartesian coordinates.
theta: This is the angle in radians from the positive x-axis to the line connecting the origin (0,0) and the projection of the point onto the xy-plane. It corresponds to the angle between the positive x-axis and the line from the origin to the point (x, y) in the xy-plane.
z: This is the same in both Cartesian and cylindrical coordinates. It represents the vertical distance of the point from the xy-plane.
        Args:
            func: the function to be integrated
            variables: the variables of integration
            intervals: the intervals of integration

        Returns: the solution to the integral

        """
        log.debug(f"""\n
        Function: {func}
        Variables: {variables}
        Intervals: {intervals}\n""")
        variable_regex = re.compile(r"([a-z]+)", re.IGNORECASE)
        # check if function is in cartesian coordinates or cylindrical coordinates
        if variable_regex.search(str(func)):
            log.debug(f"""
            Variables Found => {variable_regex.search(str(func))}
            Function: {func}
            Variables: {variables}
            Intervals: {intervals}\n""")
            # convert the function to cylindrical coordinates
            func = Subscriptable(func, {x: r * cos(theta), y: r * sin(theta), z: z})
            intervals = Subscriptable(intervals, {x: r * cos(theta), y: r * sin(theta), z: z})
            log.debug(f"""
            Function: {func}
            Variables: {variables}
            Intervals: {intervals}\n
            """)
            return MultipleIntegral(func=Function(str(func.resolved)),
                                    variables=[z, r, theta],
                                    intervals=eval(str(intervals.resolved)))
        elif func.has(r) or func.has(theta) or func.has(z) or str(func) == "1":
            # _integrate the function
            return MultipleIntegral(func=func,
                                    variables=[z, r, theta],
                                    intervals=intervals)

    @staticmethod
    def solve_sphere(func: Function, variables: Union[list, tuple], intervals: Union[List, List[Tuple]]):
        cartesian_regex = re.compile(r"([xyz]+)+", re.IGNORECASE)
        spherical_regex = re.compile(fr"({'|'.join([str(a) for a in [rho, phi, theta]])})+", re.IGNORECASE)
        func = Function(str(func))
        log.debug(f"""
        Function: {func}
        Variables: {variables}
        Intervals: {intervals}
        Cartesian Test: [x**2 + y**2 + z**2] => {cartesian_regex.findall(str(x**2 + y**2 + z**2))}
        Variables Found {cartesian_regex.__str__()} => {cartesian_regex.findall(str(func)).__str__()}
        Variables Found {spherical_regex.__str__()} => {spherical_regex.findall(str(func)).__str__()}""")
        # check if function is in cartesian coordinates or spherical coordinates
        if cartesian_regex.search(str(func)):
            # convert the function to spherical coordinates
            func = Subscriptable(func, {x: rho * (sin(phi)) * (cos(theta)), y: rho * (sin(phi)) * (sin(theta)),
                                        z: rho * (cos(phi))})
            intervals = Subscriptable(intervals,
                                      {x: rho * (sin(phi)) * (cos(theta)), y: rho * (sin(phi)) * (sin(theta)),
                                       z: rho * (cos(phi))})
            variables = [rho, phi, theta]
            log.debug(f"""
            Function: {func}\n
            Variables: {variables}\n
            Intervals: {intervals}""")
            return MultipleIntegral(func=Function(str(func.resolved)),
                                    variables=variables,
                                    intervals=eval(str(intervals.resolved)))
        elif spherical_regex.findall(str(func)):
            # _integrate the function
            return MultipleIntegral(func=func,
                                    variables=[rho, phi, theta],
                                    intervals=intervals)

    @staticmethod
    def solve_polar(func: Function, intervals: Union[List[List], Tuple[Tuple]]):
        polar_regex = re.compile(fr"({'|'.join([str(a) for a in [r, theta]])})+", re.IGNORECASE)
        cartesian_regex = re.compile(r"([xyz]+)+", re.IGNORECASE)
        # check if function is in cartesian coordinates or polar coordinates
        if cartesian_regex.search(str(func)):
            # convert the function to polar coordinates
            func = Subscriptable(func, {x: r * cos(theta), y: r * sin(theta)})
            # convert the intervals to polar coordinates
            intervals = Subscriptable(intervals, {x: r * cos(theta), y: r * sin(theta)})
            # _integrate the function
            return MultipleIntegral(func=Function(str(func.resolved)),
                                    variables=[r, theta],
                                    intervals=eval(str(intervals.resolved)))
        elif polar_regex.search(str(func)):
            log.debug(f"""
            Function: {func}
            Intervals: {intervals}
            Polar Test: [r**2] => {polar_regex.findall(str(func))}
            """)
            # _integrate the function
            return MultipleIntegral(func=func,
                                    variables=[r, theta],
                                    intervals=intervals)

    @staticmethod
    def construct_integral(func: Function, variables: Union[List, Tuple], intervals: Union[List, Tuple] = None,
                           **kwargs) -> Tuple[Integral, dict]:

        try:
            func, variables, intervals = eval(str(func)), eval(str(variables)), eval(str(intervals))
            # initialize parameters in case they are None
            global integral
            sentinel = kwargs.get("sentinel", 0)
            states = kwargs.get("states", {"integrals": [], "anti_derivatives": []})
            # log the states of the function
            status = (f"""
{'-' * 100}
    function: {func}
    intervals: {intervals}
    variables: {variables}
    variable of integration: {variables[0] if len(variables) >= 1 else None}
    Sentinel: {sentinel}
    States: {states}
{'-' * 100}
            """)
            if sentinel == 0:
                log.debug("\n%s\nConstructing Integral: \n%s", "-" * 100, "-" * 100)
            else:
                log.debug("\n%s\nIntegrating Interval: \n%s", "-" * 100, "-" * 100)

            log.debug(status)
            # check if the intervals are None and Update the states
            if len(variables) > 0 and intervals is None:
                integral = Integral(func, (variables[0]))
            elif len(variables) > 0 and len(intervals) > 0:
                integral = Integral(func, (variables[0], intervals[0][0], intervals[0][1]))
            # Update the states
            if len(variables) > 0:
                states["integrals"].append(integral)
                states["anti_derivatives"].append(integral.doit())
            # log the states of the function
            log.debug("\nStatus: \n%s", status)
            # run again if there are more variables to integrate over
            if len(variables) > 0 and len(intervals) > 0:
                return MultipleIntegral.construct_integral(integral, variables[1:],
                                                           intervals[1:],
                                                           **{"sentinel": sentinel + 1, "states": states})
            elif len(variables) > 0 and intervals is None:
                return MultipleIntegral.construct_integral(integral, variables[1:],
                                                           None,
                                                           **{"sentinel": sentinel + 1, "states": states})

            log.debug("\n%s\nFinished Constructing Integral: \n%s", "-" * 100, "-" * 100)
            log.debug("\nStatus: \n%s", status)
            log.debug("\n%s", "-" * 100)
            return integral, states
        except Exception as e:
            log.error(e)
            traceback.print_exc()
            raise e


class MultipleIntegral(Integrate):

    def __init__(self, func: Function, variables: Union[List, Tuple], intervals: Union[List[List], Tuple[Tuple]],
                 **kwargs):
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
                            options: double, triple, multiple, iterated, volume, surface_area, mass, center_of_mass,
                            moment_of_inertia, work, average_value, average_height, average_distance, average_radius,
                            average_width, average_length, average_depth, average_volume, average_surface_area,

                            Notes: Not all options are available for all types of integrals.

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
        self._integrate(func, variables, intervals, **kwargs)
        # self.print_data()

    def __dict__(self):
        return {
            "function": self.functions,
            "variables": self.variables,
            "intervals": self.intervals,
            "integrals": self.integrals,
            "anti-derivatives": self.anti_derivatives,
            "results": self.results,
            "solution": self.solution,
            "states": self.states,
            "type": self._type,
            "class": self.__class__.__name__,
            "module": self.__module__
        }

    def json_encoder(self, obj):
        if isinstance(obj, MultipleIntegral):
            return obj.__dict__()
        elif isinstance(obj, Expr):
            return str(obj)
        elif isinstance(obj, (list, tuple)):
            return [self.json_encoder(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: self.json_encoder(value) for key, value in obj.items()}
        elif isinstance(obj, (Integral, Function, Symbol, UndefinedFunction, Derivative, Matrix)):
            return str(obj)
        elif isinstance(obj, (Number, Rational, Sum)):
            return str(obj)
        elif isinstance(obj, (int, float, Zero)):
            return str(obj)
        elif isinstance(obj, String):
            return str(obj)
        elif isinstance(obj, (Mul, Add, Subs)):
            return str(obj)
        else:
            return obj.__dict__

    def __str__(self):
        return json.dumps(
            self.__dict__(),
            default=self.json_encoder,
            indent=4)

    def variables_of_integration(self, function: Union[str, Function], variables: Union[List, Tuple] = None):
        """
        Returns the variables of integration in the function
        Args:
            variables: the variables of integration
            function: the function to be integrated

        Returns: the variables of integration in the function
        """
        variables = self.variables if variables is None else variables
        return [v for v in variables if re.search(fr'\b[{v}]\b', f'{function}') is not None]

    def print_data(self):
        """
        Prints the data for all integrals
        """
        print("Function(s):")
        for func in self.functions:
            pprint(func)
            print("\n")

        print("Variable(s):")
        for var in self.variables:
            pprint(var)
            print("\n")

        print("Interval(s):")
        for interval in self.intervals:
            pprint(interval)
            print("\n")

        print("Integral(s):")
        for integral in self.integrals:
            pprint(integral)
            print("\n")

        print("Anti-Derivative(s):")
        for anti_derivative in self.anti_derivatives:
            pprint(anti_derivative)
            print("\n")

        print("Result(s):")
        for result in self.results:
            pprint(result)
            print("\n")
