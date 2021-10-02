# medium
from typing import List

'''2021-10-1'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        # also works when negative elements exist
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(max(nums), 0)
        nums[-1] = max(0, nums[-1])
        nums[-2] = max(0, nums[-2], nums[-1])
        for i in range(len(nums)-3, -1, -1):
            nums[i] = max(nums[i]+nums[i+2], nums[i+1])
        return nums[0]