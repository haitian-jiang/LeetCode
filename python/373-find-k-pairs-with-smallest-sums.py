# medium
'''2022-01-16'''

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(nums1[0]+nums2[0], 0, 0)]
        in_heap = {(0,0)}
        result = []
        for i in range(k):
            if not heap:
                break
            value, i1, i2 = heapq.heappop(heap)
            in_heap.discard((i1, i2))
            result.append([nums1[i1], nums2[i2]])
            if i1 < len(nums1) - 1 and i2 < len(nums2) and (i1+1, i2) not in in_heap:
                heapq.heappush(heap, (nums1[i1+1]+nums2[i2], i1+1, i2))
                in_heap.add((i1+1, i2))
            if i1 < len(nums1) and i2 < len(nums2) - 1 and (i1, i2+1) not in in_heap:
                heapq.heappush(heap, (nums1[i1]+nums2[i2+1], i1, i2+1))
                in_heap.add((i1, i2+1))
        return result
