# hard

'''2020-08-31'''
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:  # outlet
            return True if abs(nums[0] - 24) < 0.01 else False
    
    
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
    
                reduced_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                reduced_nums.append(nums[i] + nums[j])
                if self.judgePoint24(reduced_nums):
                    return True
    
                reduced_nums[-1] = nums[i] - nums[j]
                if self.judgePoint24(reduced_nums):
                    return True
    
                reduced_nums[-1] = nums[j] - nums[i]
                if self.judgePoint24(reduced_nums):
                    return True
    
                reduced_nums[-1] = nums[i] * nums[j]
                if self.judgePoint24(reduced_nums):
                    return True
    
                if nums[j]:
                    reduced_nums[-1] = nums[i] / nums[j]
                    if self.judgePoint24(reduced_nums):
                        return True
    
                if nums[i]:
                    reduced_nums[-1] = nums[j] / nums[i]
                    if self.judgePoint24(reduced_nums):
                        return True
    
        return False
