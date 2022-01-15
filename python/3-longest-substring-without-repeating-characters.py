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

'''2022-01-15'''
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        left = right = max_len = 0
        window = set()
        while left < len(s):
            while right < len(s) and s[right] not in window:
                window.add(s[right])
                max_len = max(max_len, len(window))
                right += 1
            window.discard(s[left])
            left += 1
        return max_len