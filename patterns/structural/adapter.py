"""
*このデザインパターンについて
アダプターパターンは、クラスに異なるインターフェイスを提供する。
コンセントの形が違うところに携帯電話を充電できるケーブルのアダプターと考えることができる。
この考えに従うと、アダプタパターンは、互換性のないインターフェイスにより統合できない
クラスを統合するのに役立つ。

*この例は何をするか？
この例には、さまざまなノイズを発生させる物や動物（Dog、Cat、Human、Car）を表す
クラスがある。Adapterクラスは、このようなノイズを発生させるオリジナルの
メソッドとは異なるインターフェイスを提供する。そのため、オリジナルのインターフェース
（barkやmeowなど）は別の名前（make_noise）で利用できる。

*このパターンは実際にどこで使われているか？
Grokフレームワークは、アダプターを使用して、オブジェクト自体を変更せずに、
オブジェクトを特定のAPIで動作させる:
http://grok.zope.org/doc/current/grok_overview.html#adapters

*参照:
http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/
https://sourcemaking.com/design_patterns/adapter
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#adapter

*要約
既存のクラスのインターフェースを別のインターフェースとして使用できるようにする。
"""

from typing import Callable, TypeVar

T = TypeVar("T")


class Dog:
    def __init__(self) -> None:
        self.name = "Dog"

    def bark(self) -> str:
        return "woof!"


class Cat:
    def __init__(self) -> None:
        self.name = "Cat"

    def meow(self) -> str:
        return "meow!"


class Human:
    def __init__(self) -> None:
        self.name = "Human"

    def speak(self) -> str:
        return "'hello'"


class Car:
    def __init__(self) -> None:
        self.name = "Car"

    def make_noise(self, octane_level: int) -> str:
        return f"vroom{'!' * octane_level}"


class Adapter:
    """メソッドを置き換えることによってオブジェクトを適応させる

    使い方
    ------
    dog = Dog()
    dog = Adapter(dog, make_noise=dog.bark)
    """

    def __init__(self, obj: T, **adapted_methods: Callable):
        """オブジェクトのdictにadapted_methodsを設定"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """適応されていない呼び出しはすべてオブジェクトに渡す"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """オリジナルのオブジェクトの辞書をプリントする"""
        return self.obj.__dict__


def main():
    """
    >>> objects = []
    >>> dog = Dog()
    >>> print(dog.__dict__)
    {'name': 'Dog'}

    >>> objects.append(Adapter(dog, make_noise=dog.bark))

    >>> objects[0].__dict__['obj'], objects[0].__dict__['make_noise']
    (<...Dog object at 0x...>, <bound method Dog.bark of <...Dog object at 0x...>>)

    >>> print(objects[0].original_dict())
    {'name': 'Dog'}

    >>> cat = Cat()
    >>> objects.append(Adapter(cat, make_noise=cat.meow))
    >>> human = Human()
    >>> objects.append(Adapter(human, make_noise=human.speak))
    >>> car = Car()
    >>> objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))

    >>> for obj in objects:
    ...    print("A {0} goes {1}".format(obj.name, obj.make_noise()))
    A Dog goes woof!
    A Cat goes meow!
    A Human goes 'hello'
    A Car goes vroom!!!
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
