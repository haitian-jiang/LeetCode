# easy

'''2020-01-06'''
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(nums == []):
            return 0
        index = 0 # 从头开始删
        while(True):
            if(index == len(nums)-1): #最后一个元素时跳出循环
                break
            if(nums[index] == nums[index+1]): # 下一个元素一样，那就删掉这个元素，后面的自动到前面，所以索引不变
                nums.pop(index)
                continue
            else: # 下一个元素不一样，那就继续循环，查后面的
                index += 1
        return len(nums)