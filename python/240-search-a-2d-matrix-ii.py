# medium

'''2021-10-14'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        # like a BST
        rows = len(matrix)
        cols = len(matrix[0])
        r, c = rows-1, 0  # left bottom corner
        while matrix[r][c] != target:
            if (r, c) == (0, cols):
                return False  # till up right corner, search ends
            if matrix[r][c] < target:
                if c == cols - 1:
                    return False
                c += 1
            elif matrix[r][c] > target:
                if r == 0:
                    return False
                r -= 1
        return True