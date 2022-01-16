# medium
'''2022-01-16'''

from queue import PriorityQueue
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        pq = []
        total = 0
        day = 0
        while True:
            while pq and pq[0][0] <= day:
                heapq.heappop(pq)
            if day < len(days) and apples[day] > 0:
                heapq.heappush(pq, [day + days[day], apples[day]])
            if not pq:
                if day < len(days):
                    day += 1
                    continue
                else:
                    break
            total += 1
            day += 1
            pq[0][1] -= 1
            if pq[0][1] == 0:
                heapq.heappop(pq)
        return total

