# medium

'''2021-01-26'''
class Solution:  # O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for start in range(len(s)):
            window = set()
            for end in range(start, len(s)):
                if s[end] not in window:
                    window.add(s[end])
                    max_len = max(max_len, len(window))
                else:
                    max_len = max(max_len, len(window))
                    break
        return max_len