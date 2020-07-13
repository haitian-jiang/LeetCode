# easy

'''2020-07-13'''
from typing import List
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        for key, value in c1.items():
            if key in c2:
                intersection.extend([key] * min(c1[key], c2[key]))
        return intersection
