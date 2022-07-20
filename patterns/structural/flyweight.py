"""
*このデザインパターンについて
このパターンは、実行時にプログラムが必要とするオブジェクトの数を最小限に抑えることを
目的としている。Flyweightは、複数のコンテキストで共有されるオブジェクトであり、
共有されていないオブジェクトとは区別できない。

Flyweightの状態は、そのコンテキストの影響を受けないようにする必要がある。
これは、固有の状態として知られています。オブジェクトの状態をオブジェクトの
コンテキストから切り離すことで、Flyweightを共有できる。

*この例は何をするか？
以下の例では、初期化されたオブジェクトを格納する'オブジェクトプール'を設定する。
'カード'が作成されると、新しいカードを作成する変わりに、最初にカードがすでに
存在するかどうかを確認する。これは、プログラムによって初期化されるオブジェクトの
数を減らすことが目的である。

*参照:
http://codesnipers.com/?q=python-flyweights
https://python-patterns.guide/gang-of-four/flyweight/

*Pythonのエコシステムの例:
https://docs.python.org/3/library/sys.html#sys.intern

*要約
他の同様のオブジェクトとデータを共有することにより、メモリ使用量を最小限に抑える。
"""

import weakref


class Card:
    """Flyweightとなるクラス"""

    # シンプルな辞書であるべき。
    # WeakValueDictionaryを使用すると、ガベージコレクションは、他に参照がない場合に
    # オブジェクトを再利用できる。
    _pool: weakref.WeakValueDictionary = weakref.WeakValueDictionary()

    def __new__(cls, value, suit):
        # オブジェクトがプールに存在する場合 - それを返す
        obj = cls._pool.get(value + suit)
        # それ以外の場合 - 新しいオブジェクトを作成する（そしてそれをプールに追加する）
        if obj is None:
            obj = object.__new__(Card)
            cls._pool[value + suit] = obj
            # この行は、通常`__init__`で見られる部分を実行する
            obj.value, obj.suit = value, suit
        return obj

    # `__init__`のコメントを外し、`__new__`をコメントアウトした場合 -
    # Cardは標準になる（Flyweightではない）
    # def __init__(self, value, suit):
    #     self.value, self.suit = value, suit

    def __repr__(self):
        return f"<Card: {self.value}{self.suit}>"


def main():
    """
    >>> c1 = Card('9', 'h')
    >>> c2 = Card('9', 'h')
    >>> c1, c2
    (<Card: 9h>, <Card: 9h>)
    >>> c1 == c2
    True
    >>> c1 is c2
    True

    >>> c1.new_attr = 'temp'
    >>> c3 = Card('9', 'h')
    >>> hasattr(c3, 'new_attr')
    True

    >>> Card._pool.clear()
    >>> c4 = Card('9', 'h')
    >>> hasattr(c4, 'new_attr')
    False
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
