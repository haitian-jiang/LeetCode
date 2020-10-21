# easy
from typing import List
import random

'''2020-10-21'''
class Solution:
    def partition(self, arr, start, end) -> int:
        pivot = arr[end]
        i = start - 1
        for j in range(start, end):
            if arr[j] < pivot:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        arr[end], arr[i+1] = arr[i+1], arr[end]
        return i + 1
    
    
    def random_partition(self, arr, start, end) -> int:
        i = random.randint(start, end)
        arr[i], arr[end] = arr[end], arr[i]
        return self.partition(arr, start, end)
    
    
    def random_select(self, arr, start, end, k) -> int:
        """end is the index of the last element"""
        if start == end:
            return arr[start]
        mid = self.random_partition(arr, start, end)
        pos = mid - start + 1
        if pos == k:
            return arr[pos]
        elif pos > k:
            return self.random_select(arr, start, mid - 1, k)
        else:
            return self.random_select(arr, mid + 1, end, k - pos)
    
    
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        k_th = self.random_select(arr, 0, len(arr)-1, k)
        return arr[:k]