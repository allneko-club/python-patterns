"""
@著者: Eugene Duboviy <eugene.dubovoy@gmail.com> | github.com/duboviy

ブラックボードパターンでは、いくつかの特殊なサブシステム（知識源）が知識を集めて、
部分的または近似的なソリューションを構築する。
このように、サブシステムが連携して問題を解決する。解決策はそのパーツの合計である。

https://en.wikipedia.org/wiki/Blackboard_system
"""

import abc
import random


class Blackboard:
    def __init__(self):
        self.experts = []
        self.common_state = {
            "problems": 0,
            "suggestions": 0,
            "contributions": [],
            "progress": 0,  # パーセンテージ, 100ならタスク完了
        }

    def add_expert(self, expert):
        self.experts.append(expert)


class Controller:
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def run_loop(self):
        """
        この関数は、progressが100に達するまで実行されるループ。
        エキスパートが貢献したいかどうかをチェックしてから、そのcontributeメソッドを呼び出す。
        """
        while self.blackboard.common_state["progress"] < 100:
            for expert in self.blackboard.experts:
                if expert.is_eager_to_contribute:
                    expert.contribute()
        return self.blackboard.common_state["contributions"]


class AbstractExpert(metaclass=abc.ABCMeta):
    def __init__(self, blackboard):
        self.blackboard = blackboard

    @property
    @abc.abstractmethod
    def is_eager_to_contribute(self):
        raise NotImplementedError("Must provide implementation in subclass.")

    @abc.abstractmethod
    def contribute(self):
        raise NotImplementedError("Must provide implementation in subclass.")


class Student(AbstractExpert):
    @property
    def is_eager_to_contribute(self):
        return True

    def contribute(self):
        self.blackboard.common_state["problems"] += random.randint(1, 10)
        self.blackboard.common_state["suggestions"] += random.randint(1, 10)
        self.blackboard.common_state["contributions"] += [self.__class__.__name__]
        self.blackboard.common_state["progress"] += random.randint(1, 2)


class Scientist(AbstractExpert):
    @property
    def is_eager_to_contribute(self):
        return random.randint(0, 1)

    def contribute(self):
        self.blackboard.common_state["problems"] += random.randint(10, 20)
        self.blackboard.common_state["suggestions"] += random.randint(10, 20)
        self.blackboard.common_state["contributions"] += [self.__class__.__name__]
        self.blackboard.common_state["progress"] += random.randint(10, 30)


class Professor(AbstractExpert):
    @property
    def is_eager_to_contribute(self):
        return True if self.blackboard.common_state["problems"] > 100 else False

    def contribute(self):
        self.blackboard.common_state["problems"] += random.randint(1, 2)
        self.blackboard.common_state["suggestions"] += random.randint(10, 20)
        self.blackboard.common_state["contributions"] += [self.__class__.__name__]
        self.blackboard.common_state["progress"] += random.randint(10, 100)


def main():
    """
    >>> blackboard = Blackboard()
    >>> blackboard.add_expert(Student(blackboard))
    >>> blackboard.add_expert(Scientist(blackboard))
    >>> blackboard.add_expert(Professor(blackboard))

    >>> c = Controller(blackboard)
    >>> contributions = c.run_loop()

    >>> from pprint import pprint
    >>> pprint(contributions)
    ['Student',
     'Student',
     'Student',
     'Student',
     'Scientist',
     'Student',
     'Student',
     'Student',
     'Scientist',
     'Student',
     'Scientist',
     'Student',
     'Student',
     'Scientist',
     'Professor']
    """


if __name__ == "__main__":
    random.seed(1234)  # doctestの出力に再現性を持たせるためにシード値を設定する
    import doctest

    doctest.testmod()
