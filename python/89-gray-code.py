# medium
'''2022-01-08'''

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        left = self.grayCode(n-1)
        right = [i+(1<<(n-1)) for i in reversed(left)]
        left.extend(right)
        return left
