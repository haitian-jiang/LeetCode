class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(target in nums):
            return nums.index(target)
        else:
            if target > nums[-1]: # 比最大的大就放在最后
                return len(nums)
            for i in range(len(nums)):
                if nums[i] > target:
                    return i # 谁比它大放谁那