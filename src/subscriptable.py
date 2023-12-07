import re
import traceback

from sympy import Function, Mul, cos, sin, tan, atan, pi
from sympy.abc import x, y, z, r, theta, phi, rho

from myLogger.logger import get_logger

log = get_logger(__name__)


class Subscriptable:
    components: list
    func: Function
    resolved: str

    def __init__(self, func, substitutions=None):
        """Initialize a Subscriptable object from a Mul object.

        Args:
            func: A Mul object
            substitutions: A dictionary of substitutions to apply to the Mul object
        """
        try:
            self.func = func
            log.debug(f"""
            func: {func}
            Type of func: {type(func)}
            substitutions: {substitutions}
            """)

            # Ensure the object is a Mul object
            if not isinstance(func, Mul):
                log.debug("Object must be a Mul object. Attempting to convert to Mul object.")
                self.components = self.convert_to_mul(func)
            else:
                # Convert the Mul object to a list of its components
                self.components = list(func.args)
            log.debug(f"""
            self.components: {self.components}
            Type of self.components: {type(self.components)}
            """)

            # Apply substitutions if provided
            if substitutions:
                for key, value in substitutions.items():
                    log.debug(f"""
                    key: {key}
                    value: {value}
                    """)
                    self.components = [factor.replace(key.__str__(), f'({value.__str__()})') for factor in self.components]
                log.debug(f"""
                self.components: {self.components}
                Type of self.components: {type(self.components)}
                    """)

            # combine the components back to a string
            self.resolved = eval(self.combine_components(self.components))
            self.components = [eval(v) for v in self.components]

        except Exception as e:
            log.debug(e)
            traceback.print_exc()
            raise TypeError(f"Object must be a Mul object. Unable to convert object "
                            f"of type {type(func)} to Mul object.")

    @staticmethod
    def combine_components(components):
        """Combine the components back to a string.

        Args:
            components: A list of components

        Returns:
            A string representation of the components
        """
        try:
            # Combine the components back to a string
            combined = "".join(components)
            log.debug(f"""
            combined: {combined}
            Type of combined: {type(combined)}""")

            return combined
        except Exception as e:
            log.debug(e)
            traceback.print_exc()
            raise ValueError("Object must be a Mul object. Unable to convert to Mul object.")

    @staticmethod
    def convert_to_mul(obj):
        """Splits the object into a list of its components, including the sign of each factor.
        Args:
            obj:  The object to be converted to a Mul object

        Returns:

        """
        try:
            # Define a regex pattern to match the sign in front of each coefficient
            pattern = r'(?=[-+])'

            # Use re.split() to split the function using the regex pattern
            components = re.split(pattern, str(obj))
            log.debug(f"""
            components: {components}
            Type of components: {type(components)}""")

            return components
        except Exception as e:
            log.debug(e)
            traceback.print_exc()
            raise ValueError("Object must be a Mul object. Unable to convert to Mul object.")

    def __getitem__(self, index):
        # Make the object subscriptable
        return self.components[index]

    def __str__(self):
        # Return the string representation of the object's dictionary
        return str(self.__dict__)

