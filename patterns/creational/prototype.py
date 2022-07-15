"""
*このデザインパターンについて
このパターンは、アプリケーションに必要なクラスの数を減らすことが目的である。
サブクラスに依存する代わりに、実行時にプロトタイプのインスタンスをコピーして
オブジェクトを作成する。

これは、クラスのインスタンスがいくつかの異なる状態の組み合わせしかない場合や、
インスタンス化にコストがかかる場合に、新しい種類のオブジェクトを簡単に
導出できるため便利である。

*この例は何をするか？
アプリケーション内のプロトタイプの数が変化する可能性がある場合は、
ディスパッチャー（別名、レジストリまたはマネージャー）を保持しておくと便利。
これにより、クライアントは、新しいインスタンスのクローンを作成する前に、
ディスパッチャにプロトタイプを照会できる。

以下に、プロトタイプの3つのコピー（'default'や'objecta', 'objectb'）を含む
ディスパッチャの例を示す。

*要約
プロトタイプのクローンを作成して、新しいオブジェクトインスタンスを作成する。
"""
from __future__ import annotations

from typing import Any


class Prototype:
    def __init__(self, value: str = "default", **attrs: Any) -> None:
        self.value = value
        self.__dict__.update(attrs)

    def clone(self, **attrs: Any) -> Prototype:
        """
        プロトタイプのクローンを作成し、内部の属性ディクショナリを更新する
        """
        # Python in Practice 著:Mark Summerfield
        # 次の行の代わりにcopy.deepcopyを使用できる。
        obj = self.__class__(**self.__dict__)
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher:
    def __init__(self):
        self._objects = {}

    def get_objects(self) -> dict[str, Prototype]:
        """全てのオブジェクトを取得する"""
        return self._objects

    def register_object(self, name: str, obj: Prototype) -> None:
        """オブジェクトを登録する"""
        self._objects[name] = obj

    def unregister_object(self, name: str) -> None:
        """オブジェクトの登録を解除する"""
        del self._objects[name]


def main() -> None:
    """
    >>> dispatcher = PrototypeDispatcher()
    >>> prototype = Prototype()

    >>> d = prototype.clone()
    >>> a = prototype.clone(value='a-value', category='a')
    >>> b = a.clone(value='b-value', is_checked=True)
    >>> dispatcher.register_object('objecta', a)
    >>> dispatcher.register_object('objectb', b)
    >>> dispatcher.register_object('default', d)

    >>> [{n: p.value} for n, p in dispatcher.get_objects().items()]
    [{'objecta': 'a-value'}, {'objectb': 'b-value'}, {'default': 'default'}]

    >>> print(b.category, b.is_checked)
    a True
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
