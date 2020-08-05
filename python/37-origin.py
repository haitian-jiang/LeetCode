def print_board(board):
    for i in range(9):
        print(board[i])
    print()

def check(row) -> bool:
    for num in range(1, 10):
        if row.count(str(num)) > 1:
            return False
    return True


def is_ok(board, trial: str, r, c) -> bool:
    column = [board[_][c] for _ in range(9)]
    cube = [board[i][j] for i in range(3*(r//3), 3*(r//3)+3) for j in range(3*(c//3), 3*(c//3)+3)]
    if check(board[r]) and check(column) and check(cube):
        return True
    return False


def solve_sudo(board, r=0, c=0):
    if (r, c) == (9, 0):
        print_board(board)
        return
    if c == 8:
        new_r, new_c = r + 1, 0
    else:
        new_r, new_c = r, c + 1
    if board[r][c].isdigit():
        solve_sudo(board, new_r, new_c)
        return
    for trial in range(1, 10):
        board[r][c] = str(trial)
        if is_ok(board, str(trial), r, c):
            solve_sudo(board, new_r, new_c)
            board[r][c] = '.'
        else: board[r][c] = '.' # 对33行尝试赋值的重置

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
solve_sudo(board)

'''
优化方法
is_ok与check可换成效率更高的37.py中的is_ok，但33与34行应调换，并删去37行的重置
也可使用cur从0到81遍历，r, c = cur // 9, cur % 9
'''
'''
此代码可以得到正确答案，但不符合题目要求
如果在判断填完(r,c=9,0)后直接调用print_board打印函数栈内的board，可得到正确答案
但是如果在调用solve_sudo后调用print_board打印，将得到原来未填的board，不符合题目直接改动board的要求
原因是无论尝试的数是正确的解还是错误的解，在solve_sudo之后总会将board[r][c]重置为'.'
所以解出了正确答案后开始return，每return回上一层函数栈，会继续执行代码将正确答案重置为'.'
所以符合题目要求的解法需要分辨哪个值对应的是正确的解，并在该情况不执行重置
一种比较方便的做法就是如37.py中对函数设有布尔返回值，正确的解法会返回true
而对于上一层函数栈，一旦得到下一层的true便执行返回(return True)，便可跳过重置部分的代码
'''