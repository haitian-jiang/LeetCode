# medium
class Solution:
    def find_min_pos(self, nums, target) -> int:
        left, right, pos = 0, len(nums) - 1, int(len(nums) / 2) # 二分查找
        while True:
            if nums[pos] == target: # 检测到目标，如果是索引最小的，跳出循环
                if pos == 0 or nums[pos - 1] != target: # 短路算法，先判断是否是第一个，否则索引错误。如果前一个不相等，说明是索引最小的
                    return pos
            if left + 1 == right: # 易错点，防止左右指针指向相邻两个，更新中间指针时由于除法取整不再变化，陷入无限循环
                return left if (nums[left] == target) else right
            if nums[pos] < target:
                left = pos
                pos = int((right + left + 1) / 2)
                continue
            if nums[pos] >= target:
                right = pos
                pos = int((right + left + 1) / 2)
                continue

    def find_max_pos(self, nums,target):
        left, right, pos = 0, len(nums) - 1, int(len(nums) / 2)
        while True:
            if nums[pos] == target:
                if pos == len(nums) - 1 or nums[pos + 1] != target :
                    return pos
            if left + 1 == right:
                return right if (nums[right] == target) else left
            if nums[pos] <= target:
                left = pos
                pos = int((right + left + 1) / 2)
                continue
            if nums[pos] > target:
                right = pos
                pos = int((right + left + 1) / 2)
                continue

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        if nums[0] == target and nums[-1] == target: # 值全部相等
            return [0, len(nums) - 1]
        min_pos = self.find_min_pos(nums, target)
        max_pos = self.find_max_pos(nums, target)
        return [min_pos, max_pos]