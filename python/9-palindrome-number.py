# easy

'''2020-01-03'''
class Solution: # 不采用字符串颠倒。使用第7题颠倒数字的算法，再判断颠倒前后是否相等。
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # 带负号的显然不回文
            return False
        new_x = x
        reversed_x = 0
        while(new_x > 0):
            reversed_x *= 10
            reversed_x += (new_x%10)
            new_x //= 10
        if reversed_x == x:
            return True
        else:
            return False