"""
依存性注入（DI）は、あるオブジェクトが別のオブジェクト（クライアント）に依存性（サービス）を提供する手法。
これによりオブジェクトを分離できる: 依存するオブジェクトを別のオブジェクトに変更する必要があるという
理由だけで、クライアントコードを変更する必要はない。（オープンクローズドの原則）

依存性注入のJavaの例の一部
"xUnit Test Patterns - Refactoring Test Code" 著: Gerard Meszaros
(ISBN-10: 0131495054, ISBN-13: 978-0131495050)

次の例では、`time_provider`（サービス）がTimeDisplay（クライアント）に埋め込まれている。
そのようなサービスが高価な操作を実行した場合は、テストでそれを代用またはモックしたいと思うだろう。

class TimeDisplay(object):

    def __init__(self):
        self.time_provider = datetime.datetime.now

    def get_current_time_as_html_fragment(self):
        current_time = self.time_provider()
        current_time_as_html_fragment = "<span class=\"tinyBoldText\">{}</span>".format(current_time)
        return current_time_as_html_fragment

"""

import datetime
from typing import Callable


class ConstructorInjection:
    def __init__(self, time_provider: Callable) -> None:
        self.time_provider = time_provider

    def get_current_time_as_html_fragment(self) -> str:
        current_time = self.time_provider()
        current_time_as_html_fragment = '<span class="tinyBoldText">{}</span>'.format(
            current_time
        )
        return current_time_as_html_fragment


class ParameterInjection:
    def __init__(self) -> None:
        pass

    def get_current_time_as_html_fragment(self, time_provider: Callable) -> str:
        current_time = time_provider()
        current_time_as_html_fragment = '<span class="tinyBoldText">{}</span>'.format(
            current_time
        )
        return current_time_as_html_fragment


class SetterInjection:
    """セッターインジェクション"""

    def __init__(self):
        pass

    def set_time_provider(self, time_provider: Callable):
        self.time_provider = time_provider

    def get_current_time_as_html_fragment(self):
        current_time = self.time_provider()
        current_time_as_html_fragment = '<span class="tinyBoldText">{}</span>'.format(
            current_time
        )
        return current_time_as_html_fragment


def production_code_time_provider() -> str:
    """
    タイムプロバイダーの製品コードバージョン（この例では日時をフォーマットするための単なるラッパーである）
    """
    current_time = datetime.datetime.now()
    current_time_formatted = f"{current_time.hour}:{current_time.minute}"
    return current_time_formatted


def midnight_time_provider() -> str:
    """ハードコードされたスタブ"""
    return "24:01"


def main():
    """
    >>> time_with_ci1 = ConstructorInjection(midnight_time_provider)
    >>> time_with_ci1.get_current_time_as_html_fragment()
    '<span class="tinyBoldText">24:01</span>'

    >>> time_with_ci2 = ConstructorInjection(production_code_time_provider)
    >>> time_with_ci2.get_current_time_as_html_fragment()
    '<span class="tinyBoldText">...</span>'

    >>> time_with_pi = ParameterInjection()
    >>> time_with_pi.get_current_time_as_html_fragment(midnight_time_provider)
    '<span class="tinyBoldText">24:01</span>'

    >>> time_with_si = SetterInjection()

    >>> time_with_si.get_current_time_as_html_fragment()
    Traceback (most recent call last):
    ...
    AttributeError: 'SetterInjection' object has no attribute 'time_provider'

    >>> time_with_si.set_time_provider(midnight_time_provider)
    >>> time_with_si.get_current_time_as_html_fragment()
    '<span class="tinyBoldText">24:01</span>'
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
