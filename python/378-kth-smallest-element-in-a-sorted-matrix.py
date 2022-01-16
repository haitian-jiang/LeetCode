# medium
'''2022-01-16'''

class Solution:
    def count(self, matrix, elem):
        n = len(matrix)
        i, j = n-1, 0
        amt = 0
        while 0<=i<n and 0<=j<n:
            if matrix[i][j] <= elem:
                amt += i+1
                j += 1
            else:
                i -= 1
        return amt

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, M = matrix[0][0], matrix[-1][-1]
        while m < M:
            mid = (m+M) // 2
            if self.count(matrix, mid) >= k:  # "=" is crucial for loop ending
                M = mid
            else:
                m = mid+1  # +1 ensures loop ends and lands on an elem in matrix
        return (m+M)//2
