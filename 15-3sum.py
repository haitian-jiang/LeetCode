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

