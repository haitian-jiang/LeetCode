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


'''2020-01-29'''
class City:
    def __init__(self, num):
        self.parent = num
        self.count = 1


class Solution:  # union-find set
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        city_amt = len(isConnected)
        cities = [City(i) for i in range(city_amt)]
        def find(x):
            y = x
            while cities[y].parent != y:
                y = cities[y].parent
            while x != y:
                t = cities[x].parent
                cities[x].parent = y
                x = t
            return y
        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return
            if cities[x].count > cities[y].count:
                cities[y].parent = x
                cities[x].count += cities[y].count
            else:
                cities[x].parent = y
                cities[y].count += cities[x].count

        for i in range(city_amt):
            for j in range(i, city_amt):
                if isConnected[i][j]:
                    union(i, j)

        prov_amt = 0
        for i in range(city_amt):
            if cities[i].parent == i:
                prov_amt += 1
        return prov_amt