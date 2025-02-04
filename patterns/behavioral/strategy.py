"""
*このデザインパターンについて
アルゴリズムの仲間を定義し、それぞれをカプセル化して、互換性を持たせる。
ストラテジーにより、アルゴリズムはそれを使用するクライアントとは独立して変化する。

*要約
実行時にアルゴリズムを選択できるようにする。
"""


from __future__ import annotations

from typing import Callable


class DiscountStrategyValidator:  # チェック実行用の記述子クラス
    @staticmethod
    def validate(obj: Order, value: Callable) -> bool:
        try:
            if obj.price - value(obj) < 0:
                raise ValueError(
                    f"Discount cannot be applied due to negative price resulting. {value.__name__}"
                )
        except ValueError as ex:
            print(str(ex))
            return False
        else:
            return True

    def __set_name__(self, owner, name: str) -> None:
        self.private_name = f"_{name}"

    def __set__(self, obj: Order, value: Callable = None) -> None:
        if value and self.validate(obj, value):
            setattr(obj, self.private_name, value)
        else:
            setattr(obj, self.private_name, None)

    def __get__(self, obj: object, objtype: type = None):
        return getattr(obj, self.private_name)


class Order:
    discount_strategy = DiscountStrategyValidator()

    def __init__(self, price: float, discount_strategy: Callable = None) -> None:
        self.price: float = price
        self.discount_strategy = discount_strategy

    def apply_discount(self) -> float:
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0

        return self.price - discount

    def __repr__(self) -> str:
        return f"<Order price: {self.price} with discount strategy: {getattr(self.discount_strategy,'__name__',None)}>"


def ten_percent_discount(order: Order) -> float:
    return order.price * 0.10


def on_sale_discount(order: Order) -> float:
    return order.price * 0.25 + 20


def main():
    """
    >>> order = Order(100, discount_strategy=ten_percent_discount)
    >>> print(order)
    <Order price: 100 with discount strategy: ten_percent_discount>
    >>> print(order.apply_discount())
    90.0
    >>> order = Order(100, discount_strategy=on_sale_discount)
    >>> print(order)
    <Order price: 100 with discount strategy: on_sale_discount>
    >>> print(order.apply_discount())
    55.0
    >>> order = Order(10, discount_strategy=on_sale_discount)
    Discount cannot be applied due to negative price resulting. on_sale_discount
    >>> print(order)
    <Order price: 10 with discount strategy: None>
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
