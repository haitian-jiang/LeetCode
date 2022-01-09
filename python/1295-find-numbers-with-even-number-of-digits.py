# easy
'''2022-01-08'''

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([i for i in map(len, map(str, nums)) if i&1 == 0])

