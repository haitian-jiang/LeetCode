# medium
from typing import List

'''2020-07-13'''  # TLE
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         triples = []
#         for i in range(len(nums)-2):
#             for j in range(i+1, len(nums)-1):
#                 expect = -(nums[i] + nums[j])
#                 if expect in nums[j+1:]:
#                     triple = sorted([nums[i], nums[j], expect])
#                     if triple not in triples:
#                         triples.append(triple)
#         return triples

'''2020-07-13'''  # TLE, 卡同一个点
# def threeSum(nums: List[int]) -> List[List[int]]:
#     nums.sort()
#     if not nums or nums[0] > 0 or nums[-1] < 0:  # 全正或全负或空
#         return []
#     if nums[0] == 0 or nums[-1] == 0:  # 无正或无负
#         if nums[:3] == [0, 0, 0] or nums[-3:] == [0, 0, 0]:  # 有足够的0
#             return [[0, 0, 0]]
#         return []
# 
#     triples = []
#     left_mid = 0
#     while nums[left_mid] < 0:
#         left_mid += 1  # left_mid左边的都<0,但nums[left_mid]不<0
#     right_mid = len(nums) - 1
#     while nums[right_mid] > 0:
#         right_mid -= 1
#     if right_mid - left_mid >= 2:
#         triples.append([0, 0, 0])
# 
#     for left in range(left_mid):
#         for right in range(right_mid + 1, len(nums)):
#             two_sum = nums[left] + nums[right]
#             triple = []
#             if two_sum == 0 and 0 in nums[left_mid: right_mid + 1]:
#                 triple = [nums[left], 0, nums[right]]
#             elif two_sum < 0 and -two_sum in nums[right + 1:]:
#                 triple = [nums[left], nums[right], -two_sum]
#             elif two_sum > 0 and -two_sum in nums[left + 1: left_mid]:
#                 triple = [nums[left], -two_sum, nums[right]]
#             if triple and triple not in triples:
#                 triples.append(triple)
#     return triples

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if not nums or nums[0] > 0 or nums[-1] < 0:  # 全正或全负或空
            return []
        triples = []
        last = nums[0] - 1
        for first in range(len(nums) - 2):
            if nums[first] == last:
                continue  # 去重
            second = first + 1  # 双指针从两边向中间搜索和为nums[first]的数对
            third = len(nums) - 1
            while second < third:
                sum = nums[first] + nums[second] + nums[third]
                current_second = nums[second]
                current_third = nums[third]
                if sum < 0:
                    while nums[second] == current_second and second < len(nums) - 1:  # 防止越界
                        second += 1  # 去重
                    continue
                elif sum > 0:
                    while nums[third] == current_third and third > 0:  # 防止越界
                        third -= 1  # 去重
                    continue
                else:
                    triples.append( [nums[first], nums[second], nums[third]] )
                    while nums[second] == current_second and second < len(nums) - 1:
                        second += 1
                    while nums[third] == current_third and third > 0:
                        third -= 1
            last = nums[first]  # 更新上一个first
        return triples
