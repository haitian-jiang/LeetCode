# medium
from typing import List

'''2021-01-29'''
class Solution:  # DFS
    visited = []

    def dfs(self, Graph: List[List[int]], u: int):
        node_amt = len(Graph)
        for v in range(node_amt):
            if Graph[u][v] and not self.visited[v]:
                self.visited[v] = 1
                self.dfs(Graph, v)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        city_amt = len(isConnected)
        prov_amt = 0
        self.visited = [0] * city_amt
        for city in range(city_amt):
            if not self.visited[city]:
                prov_amt += 1
                self.dfs(isConnected, city)
        return prov_amt