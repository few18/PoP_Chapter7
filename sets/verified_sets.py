"""Module implements different types of verified sets."""
import numbers


class VerifiedSet(set):
    """Parent class of verified sets."""

    def __init__(self, value):
        """Method to initialise set."""
        if self._verify(value):
            super().__init__(value)

    def _verify(self, value):
        """Placeholder for later methods."""
        raise NotImplementedError

    def add(self, value):
        """Method to add verified value to set."""
        if self._verify(value):
            super().add(value)

    def update(self, value):
        """Method to update set with verified value."""
        if self._verify(value):
            super().update(value)

    def symmetric_difference_update(self, value):
        """Method to make symmetric difference update."""
        if self._verify(value):
            super().symmetric_difference_update(value)

    def union(self, other):
        """Mehtod returns union of verified sets."""
        if self._verify(other):
            return type(self)(super().union(other))

    def intersection(self, other):
        """Method returns intersection of set with other set."""
        if self._verify(other):
            return type(self)(super().intersection(other))

    def difference(self, other):
        """Method returns difference between set and other set."""
        if self._verify(other):
            return type(self)(super().difference(other))

    def symmetric_difference(self, other):
        """Method returns the symmetric difference."""
        if self._verify(other):
            return type(self)(super().symmetric_difference(other))

    def copy(self):
        """Returns copy of the set."""
        return type(self)(super().copy())


class IntSet(VerifiedSet):
    """Class of verified sets of integers."""

    def _verify(self, value):
        """Method to check all elements are integers."""
        if isinstance(value, numbers.Integral):
            return True
        for val in value:
            if not isinstance(val, numbers.Integral):
                raise TypeError(f"IntSet expected an {type(1)}, got a {type(val)}.")
        return True


class UniquenessError(KeyError):
    pass


class UniqueSet(VerifiedSet):
    """Class of sets with unique values."""

    def _verify(self, value):
        """Check value not already in set."""
        if isinstance(value, numbers.Number):
            if set.__contains__(self, value):
                raise UniquenessError("Element already in set.")
        else:
            for val in value:
                if set.__contains__(self, val):
                    raise UniquenessError("Element already in set.")

        print("didnt find anything wrong")
        return True
