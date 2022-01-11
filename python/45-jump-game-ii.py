# medium
'''2022-01-09'''
from typing import List

class Solution:
    # recursion
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) <= nums[0] + 1:
            return 1
        _, nxt = max([(nums[i]+i,i)
                      for i in range(1, min(len(nums),nums[0]+1))
                      if nums[i] or i==len(nums)-1])
        return 1 + self.jump(nums[nxt:])

    def jump(self, nums: List[int]) -> int:
        curr = jumps = 0
        while True:
            if len(nums) == 1: return 0
            if curr + nums[curr] >= len(nums) - 1:
                return jumps + 1
            # curr = max([ (nums[i]+i,i) for i in range(curr+1, min(len(nums),curr+nums[curr]+1) ) ])[1]
            # the above line is equivalent to the below segment
            # but list comprehension is time consuming and space consuming
            rrange, nxt = 0, 0
            for i in range(curr+1, min(len(nums), curr+nums[curr]+1)):
                if nums[i] + i >= rrange:
                    rrange, nxt = nums[i] + i, i
            curr = nxt
            jumps += 1
