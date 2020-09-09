# medium
from typing import List


'''2020-09-09'''
class Vertex:
    __slots__ = ['adj_list', 'index', 'in_deg', 'out_deg', 'color', 'discovery_t', 'finish_t']

    def __init__(self, index):
        self.adj_list = []
        self.index = index
        self.in_deg = self.out_deg = self.color = self.discovery_t = self.finish_t = 0

class Solution:  # use dfs to topology sort
    time = 0

    def dfs(self, graph: List[Vertex], v_ind: int) -> bool:
        self.time += 1
        graph[v_ind].discovery_t = self.time
        graph[v_ind].color = -1
        for u in graph[v_ind].adj_list:
            if graph[u].color == -1:
                return False
            if graph[u].color == 0:
                if not self.dfs(graph, u):
                    return False
        graph[v_ind].color = 1
        self.time += 1
        graph[v_ind].finish_t = self.time
        return True

    def topology_sort(self, graph) -> List:
        for root in graph:
            if root.color:
                continue
            if not self.dfs(graph, root.index):
                return []
        sorted_graph = sorted(graph, key=lambda v: v.finish_t, reverse=True)
        return [v.index for v in sorted_graph]

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List:
        G = [Vertex(i) for i in range(numCourses)]
    
        for edge in prerequisites:
            G[edge[1]].adj_list.append(edge[0])
        for v_ind in range(numCourses):
            for to_node in G[v_ind].adj_list:
                G[to_node].in_deg += 1
            G[v_ind].out_deg = len(G[v_ind].adj_list)
    
        in_degree = [v.in_deg for v in G]
        out_degree = [v.out_deg for v in G]
        if 0 not in in_degree or 0 not in out_degree:  # not DAG
            return []
    
        return self.topology_sort(G)



'''2020-09-09'''
import queue
class Solution:  # use bfs, class Vertex is the same as the upper one
    def topology_sort(self, graph: List[Vertex], in_degree: List[int]) -> List:
        Q = queue.Queue()
        sorted_vert = []
        for v_ind in range(len(in_degree)):
            if in_degree[v_ind] == 0:
                Q.put(v_ind)
        while not Q.empty():
            curr_ind = Q.get()
            sorted_vert.append(curr_ind)
            in_degree[curr_ind] = -1  # 从图中删除该节点
            for to_ind in graph[curr_ind].adj_list:
                if in_degree[to_ind] >= 0:  # 说明节点还没被删除
                    in_degree[to_ind] -= 1
            for v_ind in graph[curr_ind].adj_list:  # 将新形成的入度为0的点入队，否则原来入度为0的会重复入队
                if in_degree[v_ind] == 0:
                    Q.put(v_ind)
        for v_ind in range(len(in_degree)):
            if in_degree[v_ind] > 0:
                return []
        return sorted_vert
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List:
        G = [Vertex(i) for i in range(numCourses)]
    
        for edge in prerequisites:
            G[edge[1]].adj_list.append(edge[0])
        for v_ind in range(numCourses):
            for to_node in G[v_ind].adj_list:
                G[to_node].in_deg += 1
            G[v_ind].out_deg = len(G[v_ind].adj_list)
    
        in_degree = [v.in_deg for v in G]
        out_degree = [v.out_deg for v in G]
        if 0 not in in_degree or 0 not in out_degree:  # not DAG
            return []
    
        return self.topology_sort(G, in_degree)