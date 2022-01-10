# hard
'''2022-01-09'''
from typing import List

class Solution:
    def recursion(self, start: int, rightest: int, intervals: List[List[int]]):
        if intervals[0][0] > start:
            return -1
        index = [i for i in range(len(intervals)) if intervals[i][0] <= start][-1]
        max_right = max([i[1] for i in intervals[:index+1]])
        if max_right >= rightest:
            return 1
        else:
            result = self.recursion(max_right, rightest, intervals[index+1:])
            return result if result == -1 else 1 + result
        
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = sorted([[i-ranges[i], i+ranges[i]] for i in range(n+1)])
        return self.recursion(0, n, intervals)

