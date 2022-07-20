"""
http://peter-hoffmann.com/2010/extrinsic-visitor-pattern-python-inheritance.html

*要約
アルゴリズムが動作するオブジェクト構造からそのアルゴリズムを分離する。

"Python Cookbook" (2013) 著:Brian Jones, David Beazley
で面白いレシピが見つかりました:
- "8.21. Implementing the Visitor Pattern"
- "8.22. Implementing the Visitor Pattern Without Recursion"

*Pythonのエコシステムの例:
- Python's ast.NodeVisitor: https://github.com/python/cpython/blob/master/Lib/ast.py#L250
その後、`pyflakes`のようなツールで使用される。
- `Black`というフォーマッターツールはこのパターンを実装している: https://github.com/ambv/black/blob/master/black.py#L718
"""


class Node:
    pass


class A(Node):
    pass


class B(Node):
    pass


class C(A, B):
    pass


class Visitor:
    def visit(self, node, *args, **kwargs):
        meth = None
        for cls in node.__class__.__mro__:
            meth_name = "visit_" + cls.__name__
            meth = getattr(self, meth_name, None)
            if meth:
                break

        if not meth:
            meth = self.generic_visit
        return meth(node, *args, **kwargs)

    def generic_visit(self, node, *args, **kwargs):
        print("generic_visit " + node.__class__.__name__)

    def visit_B(self, node, *args, **kwargs):
        print("visit_B " + node.__class__.__name__)


def main():
    """
    >>> a, b, c = A(), B(), C()
    >>> visitor = Visitor()

    >>> visitor.visit(a)
    generic_visit A

    >>> visitor.visit(b)
    visit_B B

    >>> visitor.visit(c)
    visit_B C
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
