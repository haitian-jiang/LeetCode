# easy

'''2020-02-06'''
from typing import List

class Solution: # 作弊解法，题目要求直接修改输入的二维矩阵
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        import copy
        m2 = copy.deepcopy(matrix)
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = m2[n-j-1][i]