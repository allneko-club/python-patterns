"""*このデザインパターンについて
ファクトリは、他のオブジェクトを作成するためのオブジェクトである。

*この例は何をするか？
このコードは、英語とギリシャ語で単語をローカライズする方法を示す。
"get_localizer"は選択した言語に応じてローカライザーを構築するファクトリ関数である。
ローカライザーオブジェクトは、ローカライズされた言語に応じて異なるクラスのインスタンスになる。
ただし、"localize"メソッドは言語に関係なく同じ方法で呼び出されるため、
メインコードはどのローカライザーがインスタンス化されるかを気にする必要はない。

*このパターンは実際にどこで使われているか？
ファクトリメソッドは、人気のあるWebフレームワークDjangoで見られる:
https://docs.djangoproject.com/en/4.0/topics/forms/formsets/
たとえば、formset_factoryを使用して様々なタイプのフォームが作成される

*参照:
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

*要約
クラスを指定せずにオブジェクトを作成する。
"""


class GreekLocalizer:
    """シンプルなローカライザ"""

    def __init__(self) -> None:
        self.translations = {"dog": "σκύλος", "cat": "γάτα"}

    def localize(self, msg: str) -> str:
        """翻訳がない場合は同じ単語を返す"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """メッセージをエコーするだけ"""

    def localize(self, msg: str) -> str:
        return msg


def get_localizer(language: str = "English") -> object:

    """ファクトリー"""
    localizers = {
        "English": EnglishLocalizer,
        "Greek": GreekLocalizer,
    }

    return localizers[language]()


def main():
    """
    # ローカライザーを作成
    >>> e, g = get_localizer(language="English"), get_localizer(language="Greek")

    # テキストを翻訳
    >>> for msg in "dog parrot cat bear".split():
    ...     print(e.localize(msg), g.localize(msg))
    dog σκύλος
    parrot parrot
    cat γάτα
    bear bear
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
