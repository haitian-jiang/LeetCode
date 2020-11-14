# medium

'''2020-11-14'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length_1 = len(text1)
        length_2 = len(text2)
        LCS = [[0 for _ in range(length_2+1)] for _ in range(length_1+1)]  # LCS[length_1][length_2]
        for i in range(1,length_1+1):
            for j in range(1, length_2+1):
                if text1[i-1] == text2[j-1]:
                    LCS[i][j] = LCS[i-1][j-1] + 1
                else:
                    LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
        return LCS[length_1][length_2]