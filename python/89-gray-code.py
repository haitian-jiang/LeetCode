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

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for i in range(n):
            for j in ans[::-1]:
                ans.append(j + (1 << i))
        return ans
