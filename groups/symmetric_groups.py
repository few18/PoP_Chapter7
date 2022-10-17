"""
Define the SymmetricGroup class.
"""
from example_code.groups import Group
import numpy as np
import numbers


class SymmetricGroup(Group):
    """Symmetric Group class, inherit properties from group class."""
    symbol = "S"

    def _validate(self, value):
        """Check that value in correct format."""

        if not isinstance(value, np.ndarray):
            raise ValueError("Entry not a numpy array.")

        if len(value) != self.n:
            raise ValueError("Array of wrong dimension.")

        for val in value:
            if not (isinstance(val, numbers.Integral) and 0 <= val < self.n):
                raise ValueError("Array entry not valid permutation")

    def operation(self, a, b):
        """Return given permutation of a."""
        return a[b]
