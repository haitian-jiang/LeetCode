# medium

'''2020-07-14'''  # TLE
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         negative = False  # 确定答案符号
#         if (dividend < 0) ^ (divisor < 0):
#             negative = True
#         dividend = abs(dividend)
#         divisor = abs(divisor)
#         ans = 0
# 
#         if dividend == 0 or dividend < divisor:  # 特殊情况优化处理
#             return 0
# 
#         amount = 0
#         while dividend >= divisor:  # 不断减去被除数并计数
#             dividend -= divisor
#             amount += 1
#         ans = -amount if negative else amount
#         return (1<<31)-1 if ans > (1<<31)-1 or ans < -(1<<31) else ans
