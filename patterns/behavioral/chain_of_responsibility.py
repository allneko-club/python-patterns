"""
*このデザインパターンについて

Chain of responsibilityは、`if ... elif ... elif ... else ...`文法の
オブジェクト指向バージョンです。条件アクションブロックを実行時に動的に再配置および
再構成できるという利点がある。

このパターンは、リクエストが処理されるまでチェーンされたレシーバーを通過できるようにすることで、
リクエストの送信者をレシーバーから切り離すことが目的である。

単純な形式のリクエストレシーバーは、単一の後継オブジェクトへの参照を保持する。
バリエーションとして、一部の受信者は「責任のツリー」を形成して、いくつかの方向に
要求を送信できる場合がある。

*要約
リクエストが処理されるまで、レシーバーのチェーンにリクエストを渡せるようにできる。
"""

from abc import ABC, abstractmethod
from typing import Optional, Tuple


class Handler(ABC):
    def __init__(self, successor: Optional["Handler"] = None):
        self.successor = successor

    def handle(self, request: int) -> None:
        """
        リクエストを処理して停止する。
        できない場合 - チェーン内の次のハンドラーを呼ぶ

        別の方法として、成功した場合でも次のハンドラーを呼び出すことができる
        """
        res = self.check_range(request)
        if not res and self.successor:
            self.successor.handle(request)

    @abstractmethod
    def check_range(self, request: int) -> Optional[bool]:
        """渡された値を事前定義された間隔と比較する"""


class ConcreteHandler0(Handler):
    """各ハンドラーは異なる場合がある
    シンプルで静的なハンドラー
    """

    @staticmethod
    def check_range(request: int) -> Optional[bool]:
        if 0 <= request < 10:
            print(f"request {request} handled in handler 0")
            return True
        return None


class ConcreteHandler1(Handler):
    """クラスの内部状態を使うハンドラー"""

    start, end = 10, 20

    def check_range(self, request: int) -> Optional[bool]:
        if self.start <= request < self.end:
            print(f"request {request} handled in handler 1")
            return True
        return None


class ConcreteHandler2(Handler):
    """ヘルパーメソッドを使ったハンドラー"""

    def check_range(self, request: int) -> Optional[bool]:
        start, end = self.get_interval_from_db()
        if start <= request < end:
            print(f"request {request} handled in handler 2")
            return True
        return None

    @staticmethod
    def get_interval_from_db() -> Tuple[int, int]:
        return (20, 30)


class FallbackHandler(Handler):
    @staticmethod
    def check_range(request: int) -> Optional[bool]:
        print(f"end of chain, no handler for {request}")
        return False


def main():
    """
    >>> h0 = ConcreteHandler0()
    >>> h1 = ConcreteHandler1()
    >>> h2 = ConcreteHandler2(FallbackHandler())
    >>> h0.successor = h1
    >>> h1.successor = h2

    >>> requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
    >>> for request in requests:
    ...     h0.handle(request)
    request 2 handled in handler 0
    request 5 handled in handler 0
    request 14 handled in handler 1
    request 22 handled in handler 2
    request 18 handled in handler 1
    request 3 handled in handler 0
    end of chain, no handler for 35
    request 27 handled in handler 2
    request 20 handled in handler 2
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
