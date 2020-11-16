# medium
from typing import List

'''2020-11-14'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1 for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], LIS[j]+1)
        return 0 if not nums else max(LIS)