import decimal
import json
import math
from dataclasses import dataclass
from typing import List, Any, Union

import numpy as np
from numpy import number
from sympy import Number

from point import Point


@dataclass
class IVector(object):
    _vector: List
    """
    Let R denote the set of real numbers. Its elements are also called 
    scalars. If n is a positive integer, then R^n is defined to be the 
    set of all sequences v1 of n real numbers:
    -  v1 = (x_1 , x_2, ... , x_n).
    The elements of R^n are called points, vectors, or n-tuples. For a 
    vector v1, the individual scalar entries x_i for i = 1, 2, . . . , n
    are called coordinates or components.

    Multivariable calculus studies function between these sets, that is, 
    function of the form f: R^n → R^m , or, more accurately, of the 
    form f: A → R^m , where A is a subset of R^n . In this context, if 
    v1 represents a typical point of R^n , the coordinates
    x_1 , x_2 , . . . , x_n are referred to as variables.
    """


class Vector(IVector):
    """Let R denote the set of real numbers. Its elements are also called 
    scalars. If n is a positive integer, then R^n is defined to be the 
    set of all sequences v1 of n real numbers:
    -  v1 = (x_1 , x_2, ... , x_n).
    The elements of R^n are called points, vectors, or n-tuples. For a 
    vector v1, the individual scalar entries x_i for i = 1, 2, . . . , n
    are called coordinates or components.

    Multivariable calculus studies function between these sets, that is,
    function of the form f: R^n → R^m , or, more accurately, of the
    form f: A → R^m , where A is a subset of R^n . In this context, if 
    v1 represents a typical point of R^n , the coordinates
    x_1 , x_2 , . . . , x_n are referred to as variables.

    Args:
        vector List: a list of real numbers or coordinates.
    """

    def __init__(self, vector: Union[List, IVector] = None):
        if isinstance(vector, IVector):
            self._vector = vector._vector
        elif isinstance(vector, list):
            self._vector = np.array([v for v in vector])  # type: ignore
        else:
            self._vector = []

    def __dict__(self):
        return {
            "vector": self._vector,
        }

    def __str__(self):
        return str(self.__dict__())

    def __add__(self, other: IVector):
        return Vector(self.addition(self._vector, other._vector))

    def __sub__(self, other: IVector):
        return Vector(self.subtraction(self._vector, other._vector))

    def __mul__(self, other: IVector):
        if isinstance(other, int):
            return sum([other * x for x in self._vector])
        elif isinstance(other, float):
            return sum([other * x for x in self._vector])
        elif isinstance(other, IVector):
            return Vector.dot(self._vector, other._vector)
        else:
            raise ValueError("Invalid type.")

    def __rmul__(self, other: IVector):
        return self.__mul__(other)

    def subtraction(self, v1: List, v2: List):
        """Subtraction: v − y = (x_1 − y_1 , x_2 − y_2 , . . . , x_n − y_n ).
        Args:
            v1 (list): an array of scalar values. Defaults to array.
            v2 (list): an array of scalar values. Defaults to array.
        """
        try:
            #printv1, v2, self._vector)
            if len(v1) == len(v2):
                return [x - y for x, y in zip(v1, v2)]
            else:
                raise ValueError("Length of v1 and v2 must be equal.")
        except ValueError as e:
            #printe)
            return None

    def addition(self, v1: List, v2: List):
        """Addition: v + y = (x_1 + y_1 , x_2 + y_2 , . . . , x_n + y_n ).
        Geometrically, v is a point in the plane plotted in the usual way. In particular,
        the origin (0, 0) is called the zero vector and is denoted by 0. Alternatively,
        we may visualize v by drawing the arrow starting at (0, 0) and ending at (x_1 , x_2 ).

        Given two vectors v = (x_1 , x_2 ) and y = (y_1 , y_2 ) in R^2 , the sum v + y as defined above is the
        point that result from adding the displacements in each of the horizontal and vertical directions,
        respectively. For instance, if v = (1, 2) and y = (3, 4), then v + y = (4, 6). Thinking of v and y as
        arrows emanating from 0, this places v + y at the vertex opposite the origin in the parallelogram
        determined by v and y, as on the left of Figure 1.1. If we think of v + y as an arrow as well, it is
        one of the diagonals of the parallelogram, as shown on the right.

        Another way to reach v + y is to move the arrow representing y so that it retains the same
        length and direction but begins at the endpoint of v. This is called a “translation” of the original
        vector y. Then v + y is the destination if you go along v followed by the translated version of
        y, as illustrated in Figure 1.2, like following two displacements v and y in succession.
        Args:
            v1 (list): an array of scalar values. Defaults to array.
            v2 (list): an array of scalar values. Defaults to array.
        """
        try:
            if len(v1) == len(v2):
                return [x + y for x, y in zip(v1, v2)]
            else:
                raise ValueError("Length of v1 and v2 must be equal.")
        except ValueError as e:
            #printe)
            return None

    @classmethod
    def dot(cls, v1: List, v2: List):
        """Dot Product: v · y = x_1 y_1 + x_2 y_2 + ... + x_n y_n .
        Args:
            v1 (list): an array of scalar values. Defaults to array.
            v2 (list): an array of scalar values. Defaults to array.
        """
        try:
            #printf"v1: {v1}, v2: {v2}")
            if len(v1) == len(v2):
                return sum([x * y for x, y in zip(v1, v2)])
            else:
                raise ValueError("Length of v1 and v2 must be equal.")
        except ValueError as e:
            #printe)
            return None

    @classmethod
    def cross(cls, v1: Union[List, IVector], v2: Union[List, IVector]):
        """Cross Product: x × y = (x_2 y_3 − x_3 y_2 , x_3 y_1 − x_1 y_3 , x_1 y_2 − x_2 y_1 ).

        The cross product also called the vector product is a vector that is perpendicular to both x and y
        and thus normal to the plane containing them. The direction of the cross product is determined by
        the right-hand rule:

        - if you curl the fingers of your right hand in the direction from x to y, then your thumb points
        in the direction of x × y. The magnitude of the cross product is given by the area of the parallelogram
        determined by x and y. In particular, if x and y are perpendicular, then x × y is the vector of length
        ||x|| ||y|| pointing in the direction determined by the right-hand rule. If x and y are parallel, then
        x × y = 0.
        Args:
            v1 (list): an array of scalar values. Defaults to array.
            v2 (list): an array of scalar values. Defaults to array.
        """
        try:
            if isinstance(v1, IVector) and isinstance(v2, IVector):
                v1 = v1._vector
                v2 = v2._vector
            elif isinstance(v1, Point) and isinstance(v2, Point):
                v1 = v1.values
                v2 = v2.values

            if len(v1) == 2 and len(v2) == 2:  # 2D vector cross product
                cross = v1[0] * v2[1] - v1[1] * v2[0]
            elif len(v1) == 3 and len(v2) == 3:  # 3D vector cross product
                cross = [
                    v1[1] * v2[2] - v1[2] * v2[1],
                    v1[2] * v2[0] - v1[0] * v2[2],
                    v1[0] * v2[1] - v1[1] * v2[0]
                ]
            else:
                raise ValueError("Length of v1 and v2 must be equal.")
            #printf'cross: {cross}')
            return cross
        except ValueError as e:
            #printe)
            return None

    def magnitude(self, v: List = None):
        """Magnitude: ||v1|| = √(x_1^2 + x_2^2 + ... + x_n^2).
        Args:
            v (list): an array of scalar values. Defaults to array.
        """
        try:
            v = v if v is not None else self._vector
            #printf'Input: {v}')
            if v is None:
                raise ValueError("Vector is None.")
            v = self._strip(v, ["*", "x", "y", "z", "i", "j", "k", "(", ")", "[", "]", "{", "}", "+", ",", "-"])
            product = sum(pow(x, 2) for x in v)
            #printf'product: sqrt({product})')
            product = math.sqrt(product)
            #printf'product: {product}')
            return product
        except ValueError as e:
            #printe)
            return None

    def _strip(self, v: List, chars: List):
        """Strip the scalar value from the vector.
        Args:
            v (Any): a scalar value.
        """
        try:
            new_v = []  # new vector
            #printf'strip input: {v}')
            if isinstance(v, Number):  # if v is a scalar value
                v = [v]  # convert to list
            for vi in v:  # for each element in v (list)
                # #printf'Before: {vi}')
                if isinstance(vi, (number, int, float)):  # if the element is a scalar value
                    # #printf'Number: {vi}')
                    new_v.append(float(vi))  # add the element to the new vector
                    continue
                for c in chars:  # for each character in chars (list)
                    vi = str(vi).replace(c, "")  # remove the character from the element
                # #printf'After replace: {vi}')
                if f'{vi}'.__contains__(" "):  # if the element contains a space
                    # #printf'Before split : {vi}')
                    vi = f'{vi}'.split(" ")  # split the element by space
                    vi = [float(a) for a in vi if a != ""]  # remove empty string
                    new_v.extend(vi)  # add the element to the new vector
                elif isinstance(vi, Number):  # if the element is a scalar value
                    new_v.append(float(vi))  # add the element to the new vector
                elif isinstance(vi, list):  # if the element is a list
                    new_v.extend(self._strip(vi, chars))  # add the element to the new vector
                # #printf'After split: {vi}')
            # #printf'Stripped: {new_v}')
            return new_v
        except ValueError as e:
            #printe)
            return None

    def component(self, x: List, y: List):
        """Component: The component of v1 in the direction of v2 is the scalar projection of
        v1 onto v2, denoted by comp_y v1, and is given by:

         - comp_y v1 = (v1 · v2)/||v2|| = (x_1 y_1 + x_2 y_2 + ... + x_n y_n )/||v2||
         
        Args:
            x (list): an array of scalar values. Defaults to array.
            y (list): an array of scalar values. Defaults to array.
        """
        try:
            return sum([x * y for x, y in zip(x, y)]) / self.magnitude(y)
        except ValueError as e:
            #printe)
            return None


###############################################################################
if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([3, 4, 5, ])
    v = Vector.cross(v1, v2)
