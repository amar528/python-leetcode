import collections
from typing import List


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = self.build_graph(equations, values)

        def dfs(start, end, visited):

            # base case - we have already visited this node, or it is not a valid node
            if start in visited or start not in graph:
                return -1.0

            # base case - we have reached the target node
            if start == end:
                return 1.0

            # mark this node as visited
            visited.add(start)

            # visit each neighbour recursively via dfs
            for neighbour, weight in graph[start]:
                path_result = dfs(neighbour, end, visited)
                if path_result != -1.0:
                    # valid path result, so multiple by the current edge
                    return weight * path_result

            # no valid path found
            return -1.0

        # for each query, call dfs on the query's start and end nodes
        return [dfs(start, end, set()) for start, end in queries]

    def build_graph(self, equations, values):

        graph = collections.defaultdict(list)

        for i in range(len(equations)):
            a, b = equations[i]
            v = values[i]

            graph[a].append((b, v))
            graph[b].append((a, 1 / v))

        return graph
