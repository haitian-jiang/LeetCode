'''2020-07-05'''
import re
from typing import List


def do_math(operand1: int, operator: str, operand2: int) -> int:
    if operator == '+':
        return operand1 + operand2
    if operator == '-':
        return operand1 - operand2
    if operator == '*':
        return operand1 * operand2
    if operator == '/':
        return operand1 / operand2


def evalRPN(rpn_expr) -> int:
    operand_stack = []  # 用来存储操作数的栈
    for token in rpn_expr:  # 索引，用来遍历后缀表达式
        if token.isdigit() or token[1:].isdigit():  # 判断是否为操作数，负数去掉最前面的负号
            operand_stack.append(int(token))
        else:  # 为操作符
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            operand_stack.append(do_math(operand1, token, operand2))
    return operand_stack[0]


def expr2RPN(mid_expr: List[str]) -> List[str]:
    priority = {'*': 2, '/': 2, '+': 1, '-': 1}
    rpn = []  # 初始化逆波兰表达式列表
    operator_stack = []
    for token in mid_expr:
        if token.isdigit():
            rpn.append(token)  # 直接进入rpn
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                rpn.append(operator_stack.pop())  # 将括号内的操作符全部放入逆波兰表达式
            operator_stack.pop()  # 弹出'('
        else:  # token为运算符
            while operator_stack and operator_stack[-1] != '(' and priority[operator_stack[-1]] >= priority[token]:
            # 短路算法，先判断是否非空。把优先级高的运算符先放入逆波兰表达式
                rpn.append(operator_stack.pop())  # 由于+和-优先级相同，要先把前面的符号放入逆波兰表达式
            operator_stack.append(token)
    while operator_stack:
        rpn.append(operator_stack.pop())  # 将剩余的运算符全部弹出放入逆波兰表达式
    return rpn


def calculate(s: str) -> int:
    s = s.replace(' ', '')  # 去除没有用的空格符
    mid_expr_list = re.split(r'([-+*/()])', s)  # -不能放在中间，否则要转义
    mid_expr_list = list(filter(bool, mid_expr_list))  # 去除列表中的空串，bool('') -> False
    rpn_list = expr2RPN(mid_expr_list)
    return evalRPN(rpn_list)


if __name__ == '__main__':
    f = open('表达式样例.txt')
    for a in f:
        print(a[:-1])
        print(calculate(a[:-1]), eval(a[:-1]))
        print()
    f.close()
