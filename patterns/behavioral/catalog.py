"""
initで渡されたパラメーターに応じて異なる静的関数を使用するクラス。
複数の状態ではなく、単一の辞書を使用していることに注意する。
"""

__author__ = "Ibrahim Diop <ibrahim@sikilabs.com>"


class Catalog:
    """初期化パラメーター応じて実行される複数の静的メソッドのカタログ"""

    def __init__(self, param: str) -> None:

        # 実行する静的メソッドを決定するために使用される辞書。また、実行できる
        # パラメーター値を格納するためにも使用される。
        self._static_method_choices = {
            "param_value_1": self._static_method_1,
            "param_value_2": self._static_method_2,
        }

        # パラメータ値を検証するための簡単なテスト
        if param in self._static_method_choices.keys():
            self.param = param
        else:
            raise ValueError(f"Invalid Value for Param: {param}")

    @staticmethod
    def _static_method_1() -> None:
        print("executed method 1!")

    @staticmethod
    def _static_method_2() -> None:
        print("executed method 2!")

    def main_method(self) -> None:
        """
        self.paramの値に応じて、_static_method_1または_static_method_2を実行する
        """
        self._static_method_choices[self.param]()


# さまざまなレベルのメソッドの代替実装法
class CatalogInstance:

    """初期化パラメータに応じて実行される複数のメソッドのカタログ"""

    def __init__(self, param: str) -> None:
        self.x1 = "x1"
        self.x2 = "x2"
        # パラメータ値を検証するための簡単なテスト
        if param in self._instance_method_choices:
            self.param = param
        else:
            raise ValueError(f"Invalid Value for Param: {param}")

    def _instance_method_1(self) -> None:
        print(f"Value {self.x1}")

    def _instance_method_2(self) -> None:
        print(f"Value {self.x2}")

    _instance_method_choices = {
        "param_value_1": _instance_method_1,
        "param_value_2": _instance_method_2,
    }

    def main_method(self) -> None:
        """
        self.paramの値に応じて、_instance_method_1または_instance_method_2を実行
        """
        self._instance_method_choices[self.param].__get__(self)()  # type: ignore
        # typeを無視する理由: https://github.com/python/mypy/issues/10206


class CatalogClass:

    """初期化パラメータに応じて実行される複数のクラスメソッドのカタログ"""

    x1 = "x1"
    x2 = "x2"

    def __init__(self, param: str) -> None:
        # パラメータ値を検証するための簡単なテスト
        if param in self._class_method_choices:
            self.param = param
        else:
            raise ValueError(f"Invalid Value for Param: {param}")

    @classmethod
    def _class_method_1(cls) -> None:
        print(f"Value {cls.x1}")

    @classmethod
    def _class_method_2(cls) -> None:
        print(f"Value {cls.x2}")

    _class_method_choices = {
        "param_value_1": _class_method_1,
        "param_value_2": _class_method_2,
    }

    def main_method(self):
        """
        self.paramの値に応じて、_class_method_1または_class_method_2を実行
        """
        self._class_method_choices[self.param].__get__(None, self.__class__)()  # type: ignore
        # typeを無視する理由: https://github.com/python/mypy/issues/10206


class CatalogStatic:

    """初期化パラメーターに応じて実行される複数の静的メソッドのカタログ"""

    def __init__(self, param: str) -> None:
        # パラメータ値を検証するための簡単なテスト
        if param in self._static_method_choices:
            self.param = param
        else:
            raise ValueError(f"Invalid Value for Param: {param}")

    @staticmethod
    def _static_method_1() -> None:
        print("executed method 1!")

    @staticmethod
    def _static_method_2() -> None:
        print("executed method 2!")

    _static_method_choices = {
        "param_value_1": _static_method_1,
        "param_value_2": _static_method_2,
    }

    def main_method(self) -> None:
        """
        self.paramの値に応じて、_static_method_1または_static_method_2を実行
        """

        self._static_method_choices[self.param].__get__(None, self.__class__)()  # type: ignore
        # typeを無視する理由: https://github.com/python/mypy/issues/10206


def main():
    """
    >>> test = Catalog('param_value_2')
    >>> test.main_method()
    executed method 2!

    >>> test = CatalogInstance('param_value_1')
    >>> test.main_method()
    Value x1

    >>> test = CatalogClass('param_value_2')
    >>> test.main_method()
    Value x2

    >>> test = CatalogStatic('param_value_1')
    >>> test.main_method()
    executed method 1!
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
