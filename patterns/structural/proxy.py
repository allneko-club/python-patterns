"""
*このデザインパターンについて
プロキシは、インターフェイスを変更せずにクラスに機能を追加する場所で使用される。
メインクラスは`Real Subject`と呼ばれる。クライアントは、コードを変更せずにプロキシまたは
実際のサブジェクトを使用する必要があるため、両方が同じインターフェイスを持っている必要がある。
実際のサブジェクトへのアクセスのロギングと制御は、プロキシパターンの使用法の一部である。

*参照:
https://refactoring.guru/design-patterns/proxy/python/example
https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Fronting.html

*要約
インターフェイスを変更せずに、リソースに機能またはロジック（例: ロギング、キャッシング、承認）
を追加する。
"""

from typing import Union


class Subject:
    """
    ドキュメントに記載されているように、クライアントはコードを変更せずにRealSubjectまたはProxyを
    使用できる様にする必要があるため、RealSubjectとProxyの両方のインターフェイスは同じである
    必要がある。

    常にこのインターフェースが必要なわけではない。重要なのは、クライアントがコードを変更せずに
    RealSubjectまたはProxyを交換しても使用できる必要があること。
    """

    def do_the_job(self, user: str) -> None:
        raise NotImplementedError()


class RealSubject(Subject):
    """
    これが主な仕事。支払いゲートウェイなどの外部サービスが良い例
    """

    def do_the_job(self, user: str) -> None:
        print(f"I am doing the job for {user}")


class Proxy(Subject):
    def __init__(self) -> None:
        self._real_subject = RealSubject()

    def do_the_job(self, user: str) -> None:
        """
        ロギングとアクセスの制御はプロキシの使用例
        """

        print(f"[log] Doing the job for {user} is requested.")

        if user == "admin":
            self._real_subject.do_the_job(user)
        else:
            print("[log] I can do the job just for `admins`.")


def client(job_doer: Union[RealSubject, Proxy], user: str) -> None:
    job_doer.do_the_job(user)


def main():
    """
    >>> proxy = Proxy()

    >>> real_subject = RealSubject()

    >>> client(proxy, 'admin')
    [log] Doing the job for admin is requested.
    I am doing the job for admin

    >>> client(proxy, 'anonymous')
    [log] Doing the job for anonymous is requested.
    [log] I can do the job just for `admins`.

    >>> client(real_subject, 'admin')
    I am doing the job for admin

    >>> client(real_subject, 'anonymous')
    I am doing the job for anonymous
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
