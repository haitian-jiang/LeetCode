# easy

'''2020-07-16'''  # 随手写一个暴力居然过了
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i * i < num:
            i += 1
        if i * i == num:
            return True
        return False
