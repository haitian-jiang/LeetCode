# medium
from typing import List

'''2020-07-14'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):  # 从第二行开始
            triangle[row][0] += triangle[row - 1][0]
            triangle[row][-1] += triangle[row - 1][-1]
            for col in range(1, row):  # row就是len(triangle[row]),遍历除去头尾的元素
                triangle[row][col] += min(triangle[row - 1][col - 1], triangle[row - 1][col])
        return min(triangle[-1])
