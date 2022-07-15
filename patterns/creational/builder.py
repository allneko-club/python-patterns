"""
*このデザインパターンについて
同属のオブジェクトを構築するプロセスを再利用できるように、
複雑なオブジェクトの作成とその表現を切り離す。
これは、オブジェクトの仕様を実際の表現から分離する必要がある場合に役立つ（一般的に抽象化のため）

*この例は何をするか？
最初の例では、建物の抽象基本クラスを使用してこのパターンを実現している。
イニシャライザー（__init__ メソッド）には必要なステップを指定し、具象サブクラスはそれらのステップを実装する。

他のプログラミング言語では、より複雑な準備が必要になる場合がある。
実際に、C++のコンストラクターでポリモーフィックな動作をすることはできない。
参照 https://stackoverflow.com/questions/1453131/how-can-i-get-polymorphic-behavior-in-a-c-constructor
これは、このPython手法が機能しないことを指している。
ポリモーフィズムは、外部のすでに構築された別のクラスのインスタンスによって提供される必要がある。

一般的に、Pythonではこれは必要ありませんが、2つ目の例はこのような手法も含まれている。

*このパターンは実際にどこで使われているか？

*参照:
https://sourcemaking.com/design_patterns/builder

*要約
複雑なオブジェクトの作成とその表現を切り離す。
"""


# 抽象ビルディング
class Building:
    def __init__(self):
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def __repr__(self):
        return "Floor: {0.floor} | Size: {0.size}".format(self)


# 具象ビルディング
class House(Building):
    def build_floor(self):
        self.floor = "One"

    def build_size(self):
        self.size = "Big"


class Flat(Building):
    def build_floor(self):
        self.floor = "More than One"

    def build_size(self):
        self.size = "Small"


# 非常に複雑な場合、構築ロジックを基本クラスの'__init__'に書くよりも、
# 別の関数（または、他のクラスのメソッド）として実装する方が望ましい場合がある。
# （基本クラスの'__init__'に書くと、具象クラスに有用なコンストラクターがないという奇妙な状況になる）

class ComplexBuilding:
    def __repr__(self):
        return "Floor: {0.floor} | Size: {0.size}".format(self)


class ComplexHouse(ComplexBuilding):
    def build_floor(self):
        self.floor = "One"

    def build_size(self):
        self.size = "Big and fancy"


def construct_building(cls):
    building = cls()
    building.build_floor()
    building.build_size()
    return building


def main():
    """
    >>> house = House()
    >>> house
    Floor: One | Size: Big

    >>> flat = Flat()
    >>> flat
    Floor: More than One | Size: Small

    # 外部のコンストラクター関数を使用:
    >>> complex_house = construct_building(ComplexHouse)
    >>> complex_house
    Floor: One | Size: Big and fancy
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
