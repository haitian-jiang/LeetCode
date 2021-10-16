# medium

'''2021-10-16'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        stop_time = float("-inf")
        feasible_cnt = 0
        for interval in intervals:
            if interval[0] >= stop_time:
                feasible_cnt += 1
                stop_time = interval[1]
        return len(intervals) - feasible_cnt