"""
@著者: Gordeev Andrey <gordeev.and.and@gmail.com>

*要約
要求処理を制御および管理する一元化されたエントリポイントを提供する。
"""


class MobileView:
    def show_index_page(self):
        print("Displaying mobile index page")


class TabletView:
    def show_index_page(self):
        print("Displaying tablet index page")


class Dispatcher:
    def __init__(self):
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()

    def dispatch(self, request):
        """
        この関数は、デバイスのタイプに基づいてリクエストをディスパッチするために使用される。
        モバイルの場合はモバイルビューが呼び出され、タブレットの場合はタブレットビューが呼び出される。
        それ以外は、"Cannot dispatch the request"というエラーメッセージが出力される。
        """
        if request.type == Request.mobile_type:
            self.mobile_view.show_index_page()
        elif request.type == Request.tablet_type:
            self.tablet_view.show_index_page()
        else:
            print("Cannot dispatch the request")


class RequestController:
    """フロントコントローラー"""

    def __init__(self):
        self.dispatcher = Dispatcher()

    def dispatch_request(self, request):
        """
        この関数はリクエストオブジェクトを受け取り、それをディスパッチャに送信する。
        """
        if isinstance(request, Request):
            self.dispatcher.dispatch(request)
        else:
            print("request must be a Request object")


class Request:
    """リクエスト"""

    mobile_type = "mobile"
    tablet_type = "tablet"

    def __init__(self, request):
        self.type = None
        request = request.lower()
        if request == self.mobile_type:
            self.type = self.mobile_type
        elif request == self.tablet_type:
            self.type = self.tablet_type


def main():
    """
    >>> front_controller = RequestController()

    >>> front_controller.dispatch_request(Request('mobile'))
    Displaying mobile index page

    >>> front_controller.dispatch_request(Request('tablet'))
    Displaying tablet index page

    >>> front_controller.dispatch_request(Request('desktop'))
    Cannot dispatch the request

    >>> front_controller.dispatch_request('mobile')
    request must be a Request object
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
