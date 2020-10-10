# medium
from typing import List

'''2020-09-07'''
class Solution:  # pure dfs to judge whether DAG or not. If see a visiting node to be visited, then not DAG
    def dfs(self, graph, vertex, visited) -> bool:
        visited[vertex] = -1
        for u in graph[vertex]:
            if visited[u] == -1:
                return False
            if visited[u] == 0:
                if not self.dfs(graph, u, visited):
                    return False
        visited[vertex] = 1
        return True
    
    def is_acyclic(self, graph, numCourses) -> bool:
        visited = [0] * numCourses  # 0 for not visited, -1 for visiting, 1 for visited
        for root in range(numCourses):
            if visited[root]:
                continue
            if not self.dfs(graph, root, visited):
                return False
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses
        out_degree = [0] * numCourses
    
        for edge in prerequisites:
            G[edge[1]].append(edge[0])
        for v in range(numCourses):
            for to_node in G[v]:
                in_degree[to_node] += 1
            out_degree[v] = len(G[v])
    
        if 0 not in in_degree or 0 not in out_degree:  # not DAG
            return False
    
        if self.is_acyclic(G, numCourses):
            return True
        return False