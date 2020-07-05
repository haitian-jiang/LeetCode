'''2020-07-05'''
# 算法:从左到右扫描列表，先遇到左操作数，再遇到右操作数，最后遇到操作符。
# 从左到右最先遇到的操作符即为最靠近操作数的操作符，是优先级最高的操作符。
# 将操作数存到栈中，一旦遇到操作符就取出栈顶的两个操作数，计算结果，推入栈中，直到遍历结束后栈内只有一个操作数，即为答案。
class Solution:
    def do_math(self, operand1: int, operator: str, operand2: int) -> int:
        if operator == '+':
            return operand1 + operand2
        if operator == '-':
            return operand1 - operand2
        if operator == '*':
            return operand1 * operand2
        if operator =='/':
            return int(operand1 / operand2)  # 题目的意思是整除，来自于C语言中/的定义，不可以使用//，由于Python的//与C的/定义不同。

    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = []  # 用来存储操作数的栈
        for pointer in range(len(tokens)):  # 索引，用来遍历tokens
            if tokens[pointer].isdigit() or tokens[pointer][1:].isdigit():  #判断是否为操作数，负数去掉负号
                operand_stack.append(int(tokens[pointer]))
            else:  # 为操作符
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                operand_stack.append(self.do_math(operand1, tokens[pointer], operand2))
        return operand_stack[0]
