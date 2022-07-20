"""
https://www.djangospin.com/design-patterns-python/mediator/

システム内のオブジェクトは、相互に直接通信するのではなくメディエーターを介して通信する。
これにより、通信するオブジェクト間の依存関係が減少し、それによって結合が減少する。

*要約
オブジェクトのセットがどのように相互作用するかをカプセル化する。
"""

from __future__ import annotations


class ChatRoom:
    """メディエータークラス"""

    def display_message(self, user: User, message: str) -> None:
        print(f"[{user} says]: {message}")


class User:
    """インスタンスが相互作用したいクラス"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.chat_room = ChatRoom()

    def say(self, message: str) -> None:
        self.chat_room.display_message(self, message)

    def __str__(self) -> str:
        return self.name


def main():
    """
    >>> molly = User('Molly')
    >>> mark = User('Mark')
    >>> ethan = User('Ethan')

    >>> molly.say("Hi Team! Meeting at 3 PM today.")
    [Molly says]: Hi Team! Meeting at 3 PM today.
    >>> mark.say("Roger that!")
    [Mark says]: Roger that!
    >>> ethan.say("Alright.")
    [Ethan says]: Alright.
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
