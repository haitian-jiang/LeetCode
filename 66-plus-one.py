class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        while(digits): # 将列表转为整数
            num *= 10
            num += digits.pop(0)
        num += 1
        output = []
        while(num): # 将整数转为列表
            output.insert(0,num%10)
            num //= 10
        return output