from typing import Dict


class RegistryHolder(type):

    REGISTRY: Dict[str, "RegistryHolder"] = {}

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        """
        ここでは、クラスの名前がキーとして使用されていますが、任意のクラスパラメータにできる。
        """
        cls.REGISTRY[new_cls.__name__] = new_cls
        return new_cls

    @classmethod
    def get_registry(cls):
        return dict(cls.REGISTRY)


class BaseRegisteredClass(metaclass=RegistryHolder):
    """
    BaseRegisteredClassから継承するクラスはすべて、dictRegistryHolder.REGISTRY
    辞書内に含まれます。そのキーはクラスの名前、値はクラス自体である。
    """


def main():
    """
    サブクラス化する前
    >>> sorted(RegistryHolder.REGISTRY)
    ['BaseRegisteredClass']

    >>> class ClassRegistree(BaseRegisteredClass):
    ...    def __init__(self, *args, **kwargs):
    ...        pass

    サブクラス化した後
    >>> sorted(RegistryHolder.REGISTRY)
    ['BaseRegisteredClass', 'ClassRegistree']
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
