# medium
'''2022-01-15'''

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        longest = [1] * len(arr)
        hash = {}
        for i in range(len(arr)-1, -1, -1):
            seq_next = arr[i] + difference
            if seq_next in hash:
                longest[i] += hash[seq_next]
            hash[arr[i]] = longest[i]
        return max(longest)
