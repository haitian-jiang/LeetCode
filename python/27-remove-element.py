# easy

'''2020-01-06'''
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while(val in nums):
            nums.remove(val)
        return len(nums)