"""
例の出所 https://en.wikipedia.org/wiki/Facade_pattern#Python

*このデザインパターンについて
ファサードパターンは、複雑なシステムへのより単純な統合インターフェイスを提供する方法。
単一のエントリポイントを提供することにより、基盤となるシステムの機能にアクセスするための
簡単な方法を提供する。この種の抽象化は、実生活で多く見られる。たとえば、ボタンを
押すだけでコンピュータの電源を入れることができるが、実際には、ボタンを押したときに
実行される多くの手順や操作がある（例: ディスクからメモリへのプログラムのロード）
この場合、ボタンは、コンピューターの電源を入れるためのすべての基本的な手順への
統一されたインターフェイスとして機能する。

*このパターンは実際にどこで使われているか？
このパターンは、isdir関数を使用する時にPython標準ライブラリで確認できる。
ユーザーはこの関数を使用してパスがディレクトリを参照しているかどうかを知るだけだが、
システムはいくつかの操作を行い、他のモジュール（例: os.stat）を呼び出して結果を出す。

*参照:
https://sourcemaking.com/design_patterns/facade
https://fkromer.github.io/python-pattern-references/design/#facade
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#facade

*要約
複雑なシステムへのよりシンプルな統合インターフェースを提供する。
"""


# 複雑なコンピューター部品
class CPU:
    """
    シンプルなCPUを表す
    """

    def freeze(self):
        print("Freezing processor.")

    def jump(self, position):
        print("Jumping to:", position)

    def execute(self):
        print("Executing.")


class Memory:
    """
    シンプルなメモリを表す
    """

    def load(self, position, data):
        print(f"Loading from {position} data: '{data}'.")


class SolidStateDrive:
    """
    シンプルなSSDを表す
    """

    def read(self, lba, size):
        return f"Some data from sector {lba} with size {size}"


class ComputerFacade:
    """
    さまざまなコンピューター部品のファサードを表す
    """

    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SolidStateDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.ssd.read("100", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()


def main():
    """
    >>> computer_facade = ComputerFacade()
    >>> computer_facade.start()
    Freezing processor.
    Loading from 0x00 data: 'Some data from sector 100 with size 1024'.
    Jumping to: 0x00
    Executing.
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
