# medium
from typing import List


'''2021-10-14'''
class Solution:
    def find132pattern_n3(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[k] < nums[j]:
                        return True
        return False

    def find132pattern_n2(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        for j in range(2, len(nums)):
            monotonic_stack = []
            for i in range(j):
                if not monotonic_stack:
                    monotonic_stack.append(nums[i])
                    continue
                else:
                    while monotonic_stack and monotonic_stack[-1] >= nums[i]:
                        monotonic_stack.pop()
                    monotonic_stack.append(nums[i])
                if monotonic_stack[-1] > nums[j] and len(monotonic_stack) > 1:
                    for n in monotonic_stack:
                        if n < nums[j]:
                            return True
        return False

    def find132pattern(self, nums: List[int]) -> bool:
        k = float("-inf")
        stack = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < k:
                return True
            while stack and stack[-1] < nums[i]:
                k = max(k, stack.pop())
            stack.append(nums[i])
        return False
