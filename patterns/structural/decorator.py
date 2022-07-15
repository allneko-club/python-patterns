"""
*このデザインパターンについて
デコレータパターンは、実装を変更せずにオブジェクトに新しい機能を動的に追加するために使用される。
新しい機能はサブクラス全体ではなく、特定のオブジェクトにのみ追加されるため、継承とは異なる。

*この例は何をするか？
この例は、対応するタグ（<b>や<i>）を追加することにより、テキストに
書式設定オプション（太字や斜体）を追加する方法を示している。
また、元のテキストが太字のラッパーに渡され、次に斜体のラッパーに渡されるため、
デコレータを次々に適用できることがわかる。

*このパターンは実際にどこで使われているか？
Grokフレームワークは、デコレータを使用して、権限やイベントへのサブスクリプションなどの
機能をメソッドに追加する:
http://grok.zope.org/doc/current/reference/decorators.html

*参照:
https://sourcemaking.com/design_patterns/decorator

*要約
クラスに影響を与えることなくオブジェクトに動作を追加する。
"""


class TextTag:
    """テキストタグの基本を表す"""

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    """<b>タグでラップする"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<b>{self._wrapped.render()}</b>"


class ItalicWrapper(TextTag):
    """<i>タグでラップする"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<i>{self._wrapped.render()}</i>"


def main():
    """
    >>> simple_hello = TextTag("hello, world!")
    >>> special_hello = ItalicWrapper(BoldWrapper(simple_hello))

    >>> print("before:", simple_hello.render())
    before: hello, world!

    >>> print("after:", special_hello.render())
    after: <i><b>hello, world!</b></i>
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
