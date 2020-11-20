# hard
from typing import List

'''2020-11-20'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)  # remove the redundant and construct an O(1) table
        longest = 0
        for i in s:  # O(n)
            if i-1 in s:  # can't be longest
                continue
            cur_longest = 1
            cur_num = i + 1
            while cur_num in s:  # O(result) = O(1)
                cur_num += 1
                cur_longest += 1
            longest = max(longest, cur_longest)
        return longest