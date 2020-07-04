'''2020-07-04'''
class Solution:
    def itoa(self, num: int, base: int) -> str:
    """uses recursion to calculate int to ascii, into the base given,
    only for positive numbers"""
        digits = '0123456789ABCDEF'  # the index indicates the value of the digit
        if num < base:
            return digits[num]
        else:
            return self.itoa(num//base, base) + digits[num%base]

    def convertToBase7(self, num: int) -> str:
        return self.itoa(num, 7) if num >= 0 else '-'+self.itoa(-num, 7)

