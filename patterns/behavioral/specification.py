"""
@著者: Gordeev Andrey <gordeev.and.and@gmail.com>

*要約
ブール論理を連鎖することにより、再結合されたビジネスロジックを提供する。
"""

from abc import abstractmethod


class Specification:
    def and_specification(self, candidate):
        raise NotImplementedError()

    def or_specification(self, candidate):
        raise NotImplementedError()

    def not_specification(self):
        raise NotImplementedError()

    @abstractmethod
    def is_satisfied_by(self, candidate):
        pass


class CompositeSpecification(Specification):
    @abstractmethod
    def is_satisfied_by(self, candidate):
        pass

    def and_specification(self, candidate):
        return AndSpecification(self, candidate)

    def or_specification(self, candidate):
        return OrSpecification(self, candidate)

    def not_specification(self):
        return NotSpecification(self)


class AndSpecification(CompositeSpecification):
    def __init__(self, one, other):
        self._one: Specification = one
        self._other: Specification = other

    def is_satisfied_by(self, candidate):
        return bool(
            self._one.is_satisfied_by(candidate)
            and self._other.is_satisfied_by(candidate)
        )


class OrSpecification(CompositeSpecification):
    def __init__(self, one, other):
        self._one: Specification = one
        self._other: Specification = other

    def is_satisfied_by(self, candidate):
        return bool(
            self._one.is_satisfied_by(candidate)
            or self._other.is_satisfied_by(candidate)
        )


class NotSpecification(CompositeSpecification):
    def __init__(self, wrapped):
        self._wrapped: Specification = wrapped

    def is_satisfied_by(self, candidate):
        return bool(not self._wrapped.is_satisfied_by(candidate))


class User:
    def __init__(self, super_user=False):
        self.super_user = super_user


class UserSpecification(CompositeSpecification):
    def is_satisfied_by(self, candidate):
        return isinstance(candidate, User)


class SuperUserSpecification(CompositeSpecification):
    def is_satisfied_by(self, candidate):
        return getattr(candidate, "super_user", False)


def main():
    """
    >>> andrey = User()
    >>> ivan = User(super_user=True)
    >>> vasiliy = 'not User instance'

    >>> root_specification = UserSpecification().and_specification(SuperUserSpecification())

    # 仕様は<name>で満たされたか
    >>> root_specification.is_satisfied_by(andrey), 'andrey'
    (False, 'andrey')
    >>> root_specification.is_satisfied_by(ivan), 'ivan'
    (True, 'ivan')
    >>> root_specification.is_satisfied_by(vasiliy), 'vasiliy'
    (False, 'vasiliy')
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
