# hard
from typing import List

'''2020-10-22'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O(m+n)
        merged = []  # big -> small
        while nums1 and nums2:
            if nums1[-1] > nums2[-1]:
                merged.append(nums1.pop())  # O(1)
            else:
                merged.append(nums2.pop())
        if nums1:
            merged.extend(nums1[::-1])
        else:
            merged.extend(nums2[::-1])
        l = len(merged)
        if l % 2:
            return merged[(l-1)//2]
        return (merged[l//2-1]+merged[l//2])/2