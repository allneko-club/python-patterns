"""
*このデザインパターンについて
コンポジットパターンは、同じタイプのオブジェクトの単一インスタンスと同じように
扱われるオブジェクトのグループを表す。コンポジットの目的は、オブジェクトを
ツリー構造に"構成"して、部分全体の階層を表すことである。コンポジットパターンを実装すると、
クライアントは個々のオブジェクトと構成を均一に扱うことができる。

*この例は何をするか？
この例では、楕円クラスまたは複数のグラフィックの合成をするクラスのいずれかの
グラフィッククラスを実装している。グラフィックはすべてプリントできる。

*このパターンは実際にどこで使われているか？
グラフィックエディタでは、形状は基本的なものから複雑なものまである。
例えば、単純な形状は線である。複雑な形状は、4つの線オブジェクトで構成される長方形である。
図形には、図形を画面にレンダリングするなどの多くの共通の操作があり、
図形は部分全体の階層に従うため、複合パターンを使用して、プログラムがすべての
図形を均一に処理できるようなる。

*参照:
https://en.wikipedia.org/wiki/Composite_pattern
https://infinitescript.com/2014/10/the-23-gang-of-three-design-patterns/

*要約
単一のインスタンスとして扱われるオブジェクトのグループを表現する。
"""

from abc import ABC, abstractmethod
from typing import List


class Graphic(ABC):
    @abstractmethod
    def render(self) -> None:
        raise NotImplementedError("You should implement this!")


class CompositeGraphic(Graphic):
    def __init__(self) -> None:
        self.graphics: List[Graphic] = []

    def render(self) -> None:
        for graphic in self.graphics:
            graphic.render()

    def add(self, graphic: Graphic) -> None:
        self.graphics.append(graphic)

    def remove(self, graphic: Graphic) -> None:
        self.graphics.remove(graphic)


class Ellipse(Graphic):
    def __init__(self, name: str) -> None:
        self.name = name

    def render(self) -> None:
        print(f"Ellipse: {self.name}")


def main():
    """
    >>> ellipse1 = Ellipse("1")
    >>> ellipse2 = Ellipse("2")
    >>> ellipse3 = Ellipse("3")
    >>> ellipse4 = Ellipse("4")

    >>> graphic1 = CompositeGraphic()
    >>> graphic2 = CompositeGraphic()

    >>> graphic1.add(ellipse1)
    >>> graphic1.add(ellipse2)
    >>> graphic1.add(ellipse3)
    >>> graphic2.add(ellipse4)

    >>> graphic = CompositeGraphic()

    >>> graphic.add(graphic1)
    >>> graphic.add(graphic2)

    >>> graphic.render()
    Ellipse: 1
    Ellipse: 2
    Ellipse: 3
    Ellipse: 4
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
