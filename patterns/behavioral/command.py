"""
コマンドパターンは、ジョブを呼び出すオブジェクトを、その方法を知っているオブジェクトから切り離す。
GoFの本で述べられているように、良い例はメニュー項目です。メニューに多くのアイテムがある。
各項目は特別なことを行う責任があり、メニュー項目が押されたときに実行メソッドを呼ぶだけで済む。
これを実現するには、各メニュー項目のexecuteメソッドを使用してコマンドオブジェクトを実装し、渡す。

*この例は何をするか？
2つのアイテムを含むメニューがある。各アイテムはファイル名を受け入れ、1つはファイルを非表示にし、
もう1つはファイルを削除する。どちらのアイテムにも元に戻すオプションがある。
各項目は、対応するコマンドを入力として受け取り、押されたときにそのexecuteメソッドを
実行するMenuItemクラスである。

*要約
コールバック関数のオブジェクト指向の実装

*Pythonのエコシステムの例:
Django HttpRequest (実行メソッドなし):
https://docs.djangoproject.com/en/2.1/ref/request-response/#httprequest-objects
"""

from typing import List, Union


class HideFileCommand:
    """
    与えられた名前のファイルを非表示にするコマンド
    """

    def __init__(self) -> None:
        # 非表示のファイルのリスト、必要に応じて元に戻す
        self._hidden_files: List[str] = []

    def execute(self, filename: str) -> None:
        print(f"hiding {filename}")
        self._hidden_files.append(filename)

    def undo(self) -> None:
        filename = self._hidden_files.pop()
        print(f"un-hiding {filename}")


class DeleteFileCommand:
    """
    与えられた名前のファイルを削除するコマンド
    """

    def __init__(self) -> None:
        # 削除されたファイルのリスト、必要に応じて元に戻す
        self._deleted_files: List[str] = []

    def execute(self, filename: str) -> None:
        print(f"deleting {filename}")
        self._deleted_files.append(filename)

    def undo(self) -> None:
        filename = self._deleted_files.pop()
        print(f"restoring {filename}")


class MenuItem:
    """
    呼び出し側クラス。メニューの項目
    """

    def __init__(self, command: Union[HideFileCommand, DeleteFileCommand]) -> None:
        self._command = command

    def on_do_press(self, filename: str) -> None:
        self._command.execute(filename)

    def on_undo_press(self) -> None:
        self._command.undo()


def main():
    """
    >>> item1 = MenuItem(DeleteFileCommand())

    >>> item2 = MenuItem(HideFileCommand())

    # 使用する`test-file`という名前のファイルを作成
    >>> test_file_name = 'test-file'

    # `test-file`を削除
    >>> item1.on_do_press(test_file_name)
    deleting test-file

    # `test-file`を復元
    >>> item1.on_undo_press()
    restoring test-file

    # `test-file`を非表示
    >>> item2.on_do_press(test_file_name)
    hiding test-file

    # `test-file`を表示
    >>> item2.on_undo_press()
    un-hiding test-file
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
