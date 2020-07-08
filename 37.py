# hard

'''2020-02-06'''
from typing import List

class Solution: # 回溯
    def is_ok(self, board, trial: str, r, c) -> bool: # 在r,c位置未填时，判断此位置填trial是否合法
        column = [board[_][c] for _ in range(9)] # r,c位置所在列
        cube = [board[i][j] for i in range(3*(r//3), 3*(r//3)+3) for j in range(3*(c//3), 3*(c//3)+3)] # r,c位置所在九宫格
        if trial in board[r] or trial in column or trial in cube:
            return False
        return True


    def solveSudoku(self, board: List[List[str]], r=0, c=0) -> bool:
        """
        Do not return anything, modify board in-place instead.
        """
        if (r, c) == (9, 0): # 求解结束，意味着之前填的空都是正确答案，填这些答案能解出数独为真
            return True
        if c == 8: # 下一个搜索位置
            new_r, new_c = r + 1, 0
        else:
            new_r, new_c = r, c + 1
        if board[r][c].isdigit(): # 若当前位置已有数，搜索下一个，跳出函数栈(return)
            return self.solveSudoku(board, new_r, new_c)
        for trial in range(1, 10): # 当前位置进行搜索
            if self.is_ok(board, str(trial), r, c): # 如果此位置填trial合法，再填(免去一次重置)
                board[r][c] = str(trial)
                if self.solveSudoku(board, new_r, new_c): # 如果此位置填此数可解后面可解，那就是此数
                    return True
        board[r][c] = '.' # 否则前面填数有错，此位置重置，返回false
        return False