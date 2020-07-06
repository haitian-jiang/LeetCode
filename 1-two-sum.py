# easy
from collections import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        answer = []
        for i in range(length): # 遍历查找解
            for j in range(i+1, length): #避免重复找解
                if nums[i]+nums[j] == target:
                    answer.append(i)
                    answer.append(j)
                    return answer