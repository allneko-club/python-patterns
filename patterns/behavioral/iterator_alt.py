"""
Pythonのイテレータプロトコルを使用したイテレータパターンの実装

*要約
コンテナを横断し、コンテナの要素にアクセスする。
"""
from __future__ import annotations


class NumberWords:
    """最大5つまで、単語番号でカウント"""

    _WORD_MAP = (
        "one",
        "two",
        "three",
        "four",
        "five",
    )

    def __init__(self, start: int, stop: int) -> None:
        self.start = start
        self.stop = stop

    def __iter__(self) -> NumberWords:  # このメソッドにより、クラスは反復可能になる
        return self

    def __next__(self) -> str:  # このメソッドにより、クラスはイテレータになる
        if self.start > self.stop or self.start > len(self._WORD_MAP):
            raise StopIteration
        current = self.start
        self.start += 1
        return self._WORD_MAP[current - 1]


# イテレーターをテストする


def main():
    """
    # 2つ数える...
    >>> for number in NumberWords(start=1, stop=2):
    ...     print(number)
    one
    two

    # 5つ数える...
    >>> for number in NumberWords(start=1, stop=5):
    ...     print(number)
    one
    two
    three
    four
    five
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
