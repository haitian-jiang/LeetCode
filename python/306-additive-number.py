# medium
'''2022-01-11'''

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for len1 in range(1, len(num) // 2 + 1):
            for len2 in range(1, len1 +len(num) // 2 + 1):
                num1, num2, rest = num[:len1], num[len1:len1+len2], num[len1+len2:]
                flag = True
                while True:
                    num3 = str(int(num1) + int(num2))
                    if not rest.startswith(num3) or num1[0]=='0' and num1 != "0" or num2[0]=='0' and num2 != "0":
                        flag = False
                        break
                    if num3 == rest:
                        return True
                    num1, num2, rest = num2, num3, rest[len(num3):]
                if not flag:
                    continue
                else:
                    return True
        return False
