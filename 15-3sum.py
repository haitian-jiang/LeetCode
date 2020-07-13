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
