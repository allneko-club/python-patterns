"""
*このデザインパターンについて
Javaや他の言語ではAbstract Factoryパターンは特定の具象クラスを必要としない、
関連/依存オブジェクトを作成するインターフェースを提供するのに役立つ。

この考え方はビジネスロジックや、プラットフォームの選択などに応じてオブジェクトの作成を抽象化する事。

パイソンでは、インターフェースはパイソンに"内蔵"されている単純なコーラブルを使う。
通常は、クラスをコーラブルとして利用できる。なぜならパイソンのクラスは第１級オブジェクトだからである。

*この例は何をするか？
ペットの作成を抽象化し、利用者が選んだファクトリー（DogやCatやrandom_animal）に応じてペットを生成する。
これは、Dog/Catとrandom_animalの両方が共通のインターフェース（生成や .speak()のコーラブルに対して）
に配慮しているため機能する。
これで、このアプリケーションはペットを抽象的に作成し、後で、利用者の基準に基づいて、猫か犬かを決定できる。


*このパターンは実際にどこで使われているか？

*参照:
https://sourcemaking.com/design_patterns/abstract_factory
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

*要約
個々のファクトリーのグループをカプセル化する方法を提供する。
"""

import random
from typing import Type


class Pet:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class Dog(Pet):
    def speak(self) -> None:
        print("woof")

    def __str__(self) -> str:
        return f"Dog<{self.name}>"


class Cat(Pet):
    def speak(self) -> None:
        print("meow")

    def __str__(self) -> str:
        return f"Cat<{self.name}>"


class PetShop:

    """ペットショップ"""

    def __init__(self, animal_factory: Type[Pet]) -> None:
        """
        pet_factoryは抽象的なファクトリーで、自由に設定できる
        """

        self.pet_factory = animal_factory

    def buy_pet(self, name: str) -> Pet:
        """
        抽象的なファクトリーを使ってペットを生成し、表示
        """

        pet = self.pet_factory(name)
        print(f"Here is your lovely {pet}")
        return pet


# 追加のファクトリー：

# 動物をランダムに生成
def random_animal(name: str) -> Pet:
    """動的に選ぶ"""
    return random.choice([Dog, Cat])(name)


# さまざまなファクトリーでペットを表示
def main() -> None:
    """
    # A Shop that sells only cats
    >>> cat_shop = PetShop(Cat)
    >>> pet = cat_shop.buy_pet("Lucy")
    Here is your lovely Cat<Lucy>
    >>> pet.speak()
    meow

    # A shop that sells random animals
    >>> shop = PetShop(random_animal)
    >>> for name in ["Max", "Jack", "Buddy"]:
    ...    pet = shop.buy_pet(name)
    ...    pet.speak()
    ...    print("=" * 20)
    Here is your lovely Cat<Max>
    meow
    ====================
    Here is your lovely Dog<Jack>
    woof
    ====================
    Here is your lovely Dog<Buddy>
    woof
    ====================
    """


if __name__ == "__main__":
    random.seed(1234)  # doctestの出力に再現性を持たせるためにシード値を設定する
    import doctest

    doctest.testmod()
