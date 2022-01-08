# hard
'''2022-01-08'''
import queue
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        i = 0
        cp = list(zip(capital, profits))
        cp.sort()
        pq = queue.PriorityQueue()
        for t in range(k):
            while i < len(cp) and cp[i][0] <= w:
                pq.put((-cp[i][1], cp[i][0]))
                i += 1
            if pq.empty():
                break
            w -= pq.get()[0]
        return w
