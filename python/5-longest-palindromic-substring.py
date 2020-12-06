# medium

'''2020-12-6'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for j in range(i)] for i in range(n, 0, -1)]  # 上三角，省空间
        start = end = 0
        max_len = 0
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n - l):
                j = i + l
                if l == 0:
                    dp[i][l] = True
                elif l == 1:
                    dp[i][l] = (s[i] == s[j])
                else:
                    dp[i][l] = (dp[i + 1][l - 2] and s[i] == s[j])
                if dp[i][l] and l + 1 > max_len:
                    max_len = l + 1
                    start = i
                    end = j
        return s[start:end+1]
