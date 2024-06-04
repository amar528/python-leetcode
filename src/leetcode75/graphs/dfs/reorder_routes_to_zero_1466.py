import collections
from typing import List


class Solution:
    def __init__(self):
        self.count = None

    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        # map the array to an adjacency list
        # the graph is directed, but we will also store the
        # inverse routes that are needed to satisfy the path to 0
        graph = collections.defaultdict(list)

        # keep track of visited nodes
        visited = set()

        # our result
        self.count = 0

        for start, end in connections:
            # city -> (neighbour, cost)
            graph[start].append((end, 1))  # original edge
            graph[end].append((start, 0))  # false edge to enable traversal

        def dfs(node):

            for neighbour, cost in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    self.count += cost
                    dfs(neighbour)

        # start dfs from city 0
        # mark 0 as already visited
        visited.add(0)
        dfs(0)

        return self.count
