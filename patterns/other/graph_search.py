class GraphSearch:

    """Pythonでのグラフ検索エミュレーション
    http://www.python.org/doc/essays/graphs/

    dfsはDepth First Searchの略
    bfsはBreadth First Searchの略"""

    def __init__(self, graph):
        self.graph = graph

    def find_path_dfs(self, start, end, path=None):
        path = path or []

        path.append(start)
        if start == end:
            return path
        for node in self.graph.get(start, []):
            if node not in path:
                newpath = self.find_path_dfs(node, end, path[:])
                if newpath:
                    return newpath

    def find_all_paths_dfs(self, start, end, path=None):
        path = path or []
        path.append(start)
        if start == end:
            return [path]
        paths = []
        for node in self.graph.get(start, []):
            if node not in path:
                newpaths = self.find_all_paths_dfs(node, end, path[:])
                paths.extend(newpaths)
        return paths

    def find_shortest_path_dfs(self, start, end, path=None):
        path = path or []
        path.append(start)

        if start == end:
            return path
        shortest = None
        for node in self.graph.get(start, []):
            if node not in path:
                newpath = self.find_shortest_path_dfs(node, end, path[:])
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def find_shortest_path_bfs(self, start, end):
        """
        幅優先探索を使用して、グラフ内の2つのノード間の最短経路を検索する。

        :param start: 開始ノード
        :type start: str または int
        :param end: 最短経路を見つけるノード
        :type end: str または int

        :returns queue_path_to_end, dist_to[end]: `start`から`end`までの
        最短経路を表すノードのリスト、およびグラフ内の各ノード（`start`を除く）
        とそのノードからの距離（ホップ数）をマッピングする辞書。
        そのようなパスが存在しない場合は、代わりに空のリストと空の辞書を返す。
        """
        queue = [start]
        dist_to = {start: 0}
        edge_to = {}

        if start == end:
            return queue

        while len(queue):
            value = queue.pop(0)
            for node in self.graph[value]:
                if node not in dist_to.keys():
                    edge_to[node] = value
                    dist_to[node] = dist_to[value] + 1
                    queue.append(node)
                    if end in edge_to.keys():
                        path = []
                        node = end
                        while dist_to[node] != 0:
                            path.insert(0, node)
                            node = edge_to[node]
                        path.insert(0, start)
                        return path


def main():
    """
    # グラフの使用例
    >>> graph = {
    ...     'A': ['B', 'C'],
    ...     'B': ['C', 'D'],
    ...     'C': ['D', 'G'],
    ...     'D': ['C'],
    ...     'E': ['F'],
    ...     'F': ['C'],
    ...     'G': ['E'],
    ...     'H': ['C']
    ... }

    # 新しいグラフ検索オブジェクトの初期化
    >>> graph_search = GraphSearch(graph)

    >>> print(graph_search.find_path_dfs('A', 'D'))
    ['A', 'B', 'C', 'D']

    # 途中から検索を開始する
    >>> print(graph_search.find_path_dfs('G', 'F'))
    ['G', 'E', 'F']

    # 到達不能ノード
    >>> print(graph_search.find_path_dfs('C', 'H'))
    None

    # 存在しないノード
    >>> print(graph_search.find_path_dfs('C', 'X'))
    None

    >>> print(graph_search.find_all_paths_dfs('A', 'D'))
    [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]
    >>> print(graph_search.find_shortest_path_dfs('A', 'D'))
    ['A', 'B', 'D']
    >>> print(graph_search.find_shortest_path_dfs('A', 'F'))
    ['A', 'C', 'G', 'E', 'F']

    >>> print(graph_search.find_shortest_path_bfs('A', 'D'))
    ['A', 'B', 'D']
    >>> print(graph_search.find_shortest_path_bfs('A', 'F'))
    ['A', 'C', 'G', 'E', 'F']

    # 途中から検索を開始する
    >>> print(graph_search.find_shortest_path_bfs('G', 'F'))
    ['G', 'E', 'F']

    # 到達不能ノード
    >>> print(graph_search.find_shortest_path_bfs('A', 'H'))
    None

    # 存在しないノード
    >>> print(graph_search.find_shortest_path_bfs('A', 'X'))
    None
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
