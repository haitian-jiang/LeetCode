# medium
'''2022-01-16'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, w):
            if board[r][c] != w[0]:
                return False
            if len(w) == 1:
                return True
            mem = board[r][c]
            board[r][c] = ""
            for r_, c_ in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0<=r_<len(board) and 0<=c_<len(board[0]) and board[r_][c_]:
                    if dfs(r_, c_, w[1:]):
                        return True
            board[r][c] = mem
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, word):
                    return True
        return False
