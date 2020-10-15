# medium

'''2020-10-15'''
class Solution:
    def Partition(self, A, start, end):
        left_ptr = start + 1
        right_ptr = end
        while True:
            while left_ptr <= right_ptr and A[left_ptr] <= A[start]:
                left_ptr += 1
            while right_ptr >= left_ptr and A[right_ptr] >= A[start]:
                right_ptr -= 1
            if left_ptr > right_ptr:
                break
            else:
                A[left_ptr], A[right_ptr] = A[right_ptr], A[left_ptr]
        A[right_ptr], A[start] = A[start], A[right_ptr]
        return right_ptr
    
    def quickSort(self, A, start, end):
        if start < end:
            mid = self.Partition(A, start, end)
            self.quickSort(A, start, mid - 1)
            self.quickSort(A, mid + 1, end)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums