"""
*このデザインパターンについて
このパターンは、オブジェクトの作成にコストがかかる場合に使用される
（そしてそれらは頻繁に作成される）ただし、一度に使用されるオブジェクトはごくわずか。
プールを使用すると、現在のインスタンスをキャッシュすることで管理できる。
プールでオブジェクトが使用可能な場合、コストのかかるオブジェクトの作成をスキップできる。
プールを使用すると、非アクティブなオブジェクトを「チェックアウト」してから返すことができる。
利用可能なものがない場合、プールは待機せずに提供するものを作成する。

*この例は何をするか？
この例では、queue.Queueを使ってプール（withステートメントで
カスタムObjectPoolオブジェクトにラップされている）を作成し、文字列が投入される。
例のとおり、最初の文字列オブジェクト"yam"は、withステートメントによって使用される。
ただし、後でプールに解放されるため、sample_queue.get()の明示的な呼び出しにより再利用される。
関数内で作成されたObjectPoolが（GCによって）削除されオブジェクトが返される時は、
"sam"でも同じことが起こる。

*このパターンは実際にどこで使われているか？

*参照:
http://stackoverflow.com/questions/1514120/python-implementation-of-the-object-pool-design-pattern
https://sourcemaking.com/design_patterns/object_pool

*要約
すぐに使用できる状態の初期化されたオブジェクトのセットを格納する。
"""


class ObjectPool:
    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.item = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, Type, value, traceback):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None


def main():
    """
    >>> import queue

    >>> def test_object(queue):
    ...    pool = ObjectPool(queue, True)
    ...    print('関数の内側: {}'.format(pool.item))

    >>> sample_queue = queue.Queue()

    >>> sample_queue.put('yam')
    >>> with ObjectPool(sample_queue) as obj:
    ...    print('with文の内側: {}'.format(obj))
    with文の内側: yam

    >>> print('with文の外側: {}'.format(sample_queue.get()))
    with文の外側: yam

    >>> sample_queue.put('sam')
    >>> test_object(sample_queue)
    関数の内側: sam

    >>> print('関数の外側: {}'.format(sample_queue.get()))
    関数の外側: sam

    if not sample_queue.empty():
        print(sample_queue.get())
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
