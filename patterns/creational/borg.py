"""
*このデザインパターンについて
ボーグパターン（モノステートパターンとも呼ばれます）は、シングルトンの動作を実装する
方法である。ただし、クラスのインスタンスを1つだけ持つのではなく、同じ状態を共有する
複数のインスタンスがある。つまり、インスタンスIDを共有するのではなく、
状態を共有することに重点が置かれる。

*この例は何をするか？
Pythonでのこのパターンの実装を理解するには、インスタンスの属性が__dict__と呼ばれる
属性ディクショナリに格納されていることを知っておくことが重要。通常、各インスタンスには
独自の辞書があるが、ボーグパターンはすべてのインスタンスが同じ辞書を持つように変更する。
この例では、__shared_state属性がすべてのインスタンス間で共有されるディクショナリである。
これは、新しいインスタンスを__init__メソッドで初期化するときに__shared_stateを
__dict__変数に割り当てることによって保証される。他の属性は通常、インスタンスの
属性ディクショナリに追加されるが、属性ディクショナリ（__shared_state）自体が
共有されるため、他の属性もすべて共有される。

*このパターンは実際にどこで使われているか？
状態の共有はデータベース接続の管理などのアプリケーションで役立つ:
https://github.com/onetwopunch/pythonDbTemplate/blob/master/database.py

*参照:
- https://fkromer.github.io/python-pattern-references/design/#singleton
- https://learning.oreilly.com/library/view/python-cookbook/0596001673/ch05s23.html
- http://www.aleax.it/5ep.html

*要約
インスタンス間で状態を共有するシングルトンのような動作を提供する。
"""
from typing import Dict


class Borg:
    _shared_state: Dict[str, str] = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class YourBorg(Borg):
    def __init__(self, state=None):
        super().__init__()
        if state:
            self.state = state
        else:
            # デフォルトの状態で最初のインスタンスを初期化
            if not hasattr(self, "state"):
                self.state = "Init"

    def __str__(self):
        return self.state


def main():
    """
    >>> rm1 = YourBorg()
    >>> rm2 = YourBorg()

    >>> rm1.state = 'Idle'
    >>> rm2.state = 'Running'

    >>> print('rm1: {0}'.format(rm1))
    rm1: Running
    >>> print('rm2: {0}'.format(rm2))
    rm2: Running

    # `state`属性が`rm2`インスタンスから変更されると、
    # `rm1`インスタンスの`state`の値も変更される
    >>> rm2.state = 'Zombie'

    >>> print('rm1: {0}'.format(rm1))
    rm1: Zombie
    >>> print('rm2: {0}'.format(rm2))
    rm2: Zombie

    # `rm1`と`rm2`は属性を共有しているが、インスタンスは同じではない
    >>> rm1 is rm2
    False

    # 新しいインスタンスも同じ共有状態を取得する
    >>> rm3 = YourBorg()

    >>> print('rm1: {0}'.format(rm1))
    rm1: Zombie
    >>> print('rm2: {0}'.format(rm2))
    rm2: Zombie
    >>> print('rm3: {0}'.format(rm3))
    rm3: Zombie

    # 新しいインスタンスは、作成中に状態を明示的に変更できる
    >>> rm4 = YourBorg('Running')

    >>> print('rm4: {0}'.format(rm4))
    rm4: Running

    # 既存のインスタンスはその変更も反映する
    >>> print('rm3: {0}'.format(rm3))
    rm3: Running
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
