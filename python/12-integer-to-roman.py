# medium
'''2022-01-04'''
class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        numbers = list(sorted(mapping.keys()))  # [1, ..., 900, 1000]
        result = ''
        while num > 0:
            if num < numbers[-1]:
                numbers.pop()
            else:
                num -= numbers[-1]
                result = result + mapping[numbers[-1]]
        return result
