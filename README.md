python パターン集
===============

パイソンで書かれたデザインパターンやイディオムのコレクション

主流のパターン
----------------

__生成に関するパターン__:

| パターン | 説明                                                         |
|:-------:|------------------------------------------------------------|
| [abstract_factory](patterns/creational/abstract_factory.py) | 特定のファクトリでジェネリック関数を使用する                                     |
| [borg](patterns/creational/borg.py) | インスタンス間で状態を共有するシングルトン                                      |
| [builder](patterns/creational/builder.py) | 複数のコンストラクターを使用する代わりに、ビルダーオブジェクトはパラメーターを受け取り、構築されたオブジェクトを返す |
| [factory](patterns/creational/factory.py) | インスタンスを作成するための特殊な関数/メソッドを委任する                              |
| [lazy_evaluation](patterns/creational/lazy_evaluation.py) | Pythonで遅延評価されたプロパティパターン                                    |
| [pool](patterns/creational/pool.py) | 同じタイプのインスタンスのグループを事前にインスタンス化して維持する                         |
| [prototype](patterns/creational/prototype.py) | 新しいインスタンスのファクトリとプロトタイプのクローンを使用する（インスタンス化に時間がかかる場合）         |

__構造に関するパターン__:

| パターン                                                        | 説明                                       |
|:------------------------------------------------------------|------------------------------------------|
| [3-tier](patterns/structural/3-tier.py)                     | データ<->ビジネスロジック<->プレゼンテーションの分離（厳密な関係）     |
| [adapter](patterns/structural/adapter.py)                   | ホワイトリストを使用して、あるインターフェイスを別のインターフェイスに適合させる |
| [bridge](patterns/structural/bridge.py)                     | インターフェイスの変更を和らげるためのクライアントとプロバイダーの仲介者     |
| [composite](patterns/structural/composite.py)               | クライアントが個々のオブジェクトと構成を均一に処理できるようにする        |
| [decorator](patterns/structural/decorator.py)               | 出力に影響を与えるために、機能を他の機能でラップする               |
| [facade](patterns/structural/facade.py)                     | 1つのクラスを他の多くのクラスへのAPIとして使用する              |
| [flyweight](patterns/structural/flyweight.py)               | 類似/同一の状態のオブジェクトを透過的に再利用する                |
| [front_controller](patterns/structural/front_controller.py) | 単一のリクエストハンドラー                            |
| [mvc](patterns/structural/mvc.py)                           | model <-> view <-> controller（非厳密な関係）    |
| [proxy](patterns/structural/proxy.py)                       | あるオブジェクトが他の何かに操作を集中させる                   |

__振る舞いに関するパターン__:

| パターン | 説明                                            |
|:-------:|-----------------------------------------------|
| [chain_of_responsibility](patterns/behavioral/chain_of_responsibility.py) | 連続するハンドラーのチェーンを適用して、データを処理する                  |
| [catalog](patterns/behavioral/catalog.py) | 一般的なメソッドは、構築パラメータに基づいてさまざまな特殊なメソッドを呼び出す       |
| [chaining_method](patterns/behavioral/chaining_method.py) | コールバックの次のオブジェクトメソッドを続行する                      |
| [command](patterns/behavioral/command.py) | 後で呼び出すコマンドと引数をバンドルする                          |
| [iterator](patterns/behavioral/iterator.py) | コンテナを横断し、コンテナの要素にアクセスする                       |
| [iterator](patterns/behavioral/iterator_alt.py) (alt. impl.)| コンテナを横断し、コンテナの要素にアクセスする                       |
| [mediator](patterns/behavioral/mediator.py) | 他のオブジェクトを接続してプロキシとして機能する方法を知っているオブジェクト        |
| [memento](patterns/behavioral/memento.py) | 以前の状態に戻るために使う曖昧なトークンを生成する                     |
| [observer](patterns/behavioral/observer.py) | データにイベント/変更の通知をするためのコールバックを提供する               |
| [publish_subscribe](patterns/behavioral/publish_subscribe.py) | ソースはイベント/データを0件以上の登録済みリスナーに配給する               |
| [registry](patterns/behavioral/registry.py) | 特定のクラスのすべてのサブクラスを追跡する                         |
| [specification](patterns/behavioral/specification.py) | ブール論理を使用してビジネスルールをチェーン化することにより、ビジネスルールを再結合できる |
| [state](patterns/behavioral/state.py) | 離散的な潜在的状態と、遷移可能な次の状態に構造化される                   |
| [strategy](patterns/behavioral/strategy.py) | 同じデータに対する選択可能な操作                              |
| [template](patterns/behavioral/template.py) | オブジェクトは構築化を負いますが、接続可能なコンポーネントを受け取る            |
| [visitor](patterns/behavioral/visitor.py) | コレクションのすべてのアイテムに対してコールバックを呼び出す                |

__テストしやすいパターン__:

| パターン | 説明                                            |
|:-------:|-----------------------------------------------|
| [dependency_injection](patterns/dependency_injection.py) | 依存性注入 ３パターン |

__基本的なパターン__:

| パターン | 説明                                              |
|:-------:|-------------------------------------------------|
| [delegation_pattern](patterns/fundamental/delegation_pattern.py) | オブジェクトは、2番目のオブジェクト（デリゲート）に委任することによってリクエストを処理する |

__その他__:

| パターン | 説明                                     |
|:-------:|----------------------------------------|
| [blackboard](patterns/other/blackboard.py) | アーキテクチャモデル、ソリューションを構築するためのさまざまなサブシステム知識の組み立て、AIアプローチ - Gang Of Fourのデザインパターンではない |
| [graph_search](patterns/other/graph_search.py) | グラフ化アルゴリズム - Gang Of Fourのデザインパターンではない |
| [hsm](patterns/other/hsm/hsm.py) | 階層型ステートマシン - Gang Of Fourのデザインパターンではない |


Videos
------
[Design Patterns in Python by Peter Ullrich](https://www.youtube.com/watch?v=bsyjSW46TDg)

[Sebastian Buczyński - Why you don't need design patterns in Python?](https://www.youtube.com/watch?v=G5OeYHCJuv0)

[You Don't Need That!](https://www.youtube.com/watch?v=imW-trt0i9I)

[Pluggable Libs Through Design Patterns](https://www.youtube.com/watch?v=PfgEU3W0kyU)


Contributing
------------
When an implementation is added or modified, please review the following guidelines:

##### Docstrings
Add module level description in form of a docstring with links to corresponding references or other useful information.

Add "Examples in Python ecosystem" section if you know some. It shows how patterns could be applied to real-world problems.

[facade.py](patterns/structural/facade.py) has a good example of detailed description,
but sometimes the shorter one as in [template.py](patterns/behavioral/template.py) would suffice.

##### Python 2 compatibility
To see Python 2 compatible versions of some patterns please check-out the [legacy](https://github.com/faif/python-patterns/tree/legacy) tag.

##### Update README
When everything else is done - update corresponding part of README.

##### Travis CI
Please run `tox` or `tox -e ci37` before submitting a patch to be sure your changes will pass CI.

You can also run `flake8` or `pytest` commands manually. Examples can be found in `tox.ini`.

## Contributing via issue triage [![Open Source Helpers](https://www.codetriage.com/faif/python-patterns/badges/users.svg)](https://www.codetriage.com/faif/python-patterns)

You can triage issues and pull requests which may include reproducing bug reports or asking for vital information, such as version numbers or reproduction instructions. If you would like to start triaging issues, one easy way to get started is to [subscribe to python-patterns on CodeTriage](https://www.codetriage.com/faif/python-patterns).
