# medium
'''2022-01-10'''

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        return self.rec(0, time, clips)

    def rec(self, start: int, time: int, intervals: List[List[int]]):
        if not intervals or intervals[0][0] > start:
            return -1
        index = [i for i in range(len(intervals)) if intervals[i][0] <= start][-1]
        max_right = max([i[1] for i in intervals[:index+1]])
        if max_right >= time:
            return 1
        else:
            r = self.rec(max_right, time, intervals[index + 1:])
            return r if r==-1 else 1+r
