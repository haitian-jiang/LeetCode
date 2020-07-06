# hard
import copy
class Solution:
    def NQueen(self, n, k, board, solution_list):
        if k == n:
            solution_list.append(copy.deepcopy(board))
            board = [-1] * n
            return
        for k_val in range(n):
            if k_val in board:
                continue
            flag = 0
            for j in range(k):
                if board[j] - k_val == j - k or board[j] - k_val == k - j:
                    flag = 1
                    break
            if flag:
                continue
            board[k] = k_val
            self.NQueen(n, k + 1, board, solution_list)
        board[k] = -1
        return
    def totalNQueens(self, n: int) -> int:
        board = [-1] * n
        solution_list = []
        self.NQueen(n, 0, board, solution_list)
        return len(solution_list)
