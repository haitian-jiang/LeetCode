'''2020-07-05'''
import re
class Solution:
    def do_math(self, operand1: int, operator: str, operand2: int) -> int:
        if operator == '+':
            return operand1 + operand2
        if operator == '-':
            return operand1 - operand2
        if operator == '*':
            return operand1 * operand2
        if operator == '/':
            return int(operand1 / operand2)  # 题目的意思是整除，来自于C语言中/的定义，不可以使用//，由于Python的//与C的/定义不同。
    
    
    def evalRPN(self, tokens) -> int:
        operand_stack = []  # 用来存储操作数的栈
        for pointer in range(len(tokens)):  # 索引，用来遍历tokens
            if tokens[pointer].isdigit() or tokens[pointer][1:].isdigit():  # 判断是否为操作数，负数去掉最前面的负号
                operand_stack.append(int(tokens[pointer]))
            else:  # 为操作符
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                operand_stack.append(self.do_math(operand1, tokens[pointer], operand2))
        return operand_stack[0]
    
    
    def expr2RPN(self, mid_expr: List[str]) -> List[str]:
        rpn = []  # 初始化逆波兰表达式列表
        operator_stack = []
        for i in range(len(mid_expr)):
            pointer = mid_expr[i]
            if pointer.isdigit():
                rpn.append(mid_expr[i])  # 直接进入rpn
            elif pointer == '(':
                operator_stack.append(pointer)
            elif pointer in '+-':
                while operator_stack and operator_stack[-1] != '(':  # 短路算法，先判断是否非空
                    rpn.append(operator_stack.pop())  # 由于+和-优先级相同，要先把前面的符号放入逆波兰表达式
                operator_stack.append(pointer)
            else:  # pointer == ')'
                while operator_stack[-1] != '(':
                    rpn.append(operator_stack.pop())  # 将括号内的操作符全部放入逆波兰表达式
                operator_stack.pop()  # 弹出'('
        while operator_stack:
            rpn.append(operator_stack.pop())  # 将剩余的运算符全部弹出放入逆波兰表达式
        return rpn
    
    
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')  # 去除没有用的空格符
        mid_expr_list = re.split(r'([-+()])', s)  # -不能放在中间，否则要转义
        mid_expr_list = list(filter(bool, mid_expr_list))  # 去除列表中的空串，bool('') -> False
        rpn_list = self.expr2RPN(mid_expr_list)
        return self.evalRPN(rpn_list)
