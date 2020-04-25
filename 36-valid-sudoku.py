import copy # 为了深拷贝board数组，切片复制为浅拷贝，给转置赋值时会出错
class Solution:
    def is_row_valid(self, board: List[List[str]]) -> bool:
        for i in range(9): # 对于每行而言
            for num in range(1,10): # 所有的数字
                if board[i].count(str(num)) > 1: # 要都只出现一次
                    return False
        return True
    
    def is_cube_valid(self,board):
        cube = [] # 从左到右，再从上到下
        for i in range(9):
            cube.append([])
        cube[0]  = [board[i][j] for i in range(3) for j in range(3)]
        cube[1]  = [board[i][j] for i in range(3) for j in range(3,6)]
        cube[2]  = [board[i][j] for i in range(3) for j in range(6,9)]
        cube[3]  = [board[i][j] for i in range(3,6) for j in range(3)]
        cube[4]  = [board[i][j] for i in range(3,6) for j in range(3,6)]
        cube[5]  = [board[i][j] for i in range(3,6) for j in range(6,9)]
        cube[6]  = [board[i][j] for i in range(6,9) for j in range(3)]
        cube[7]  = [board[i][j] for i in range(6,9) for j in range(3,6)]
        cube[8]  = [board[i][j] for i in range(6,9) for j in range(6,9)]
        return self.is_row_valid(cube)
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.is_row_valid(board):
            return False
        
        if not self.is_cube_valid(board):
            return False
        
        transpose = copy.deepcopy(board) # 求转置
        for i in range(9):
            for j in range(9):
                transpose[i][j] = board[j][i]
        if not self.is_row_valid(transpose):
            return False
        del transpose # 释放空间
        
        return True