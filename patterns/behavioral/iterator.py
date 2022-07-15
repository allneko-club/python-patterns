"""
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
ジェネレータを使用したイテレータパターンの実装

*要約
コンテナを横断し、コンテナの要素にアクセスする。
"""


def count_to(count):
    """最大5つまで、単語番号でカウント"""
    numbers = ["one", "two", "three", "four", "five"]
    yield from numbers[:count]


# ジェネレータをテストする
def count_to_two() -> None:
    return count_to(2)


def count_to_five() -> None:
    return count_to(5)


def main():
    """
    # 2つ数える...
    >>> for number in count_to_two():
    ...     print(number)
    one
    two

    # 5つ数える...
    >>> for number in count_to_five():
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
