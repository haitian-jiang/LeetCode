# hard

'''2020-10-19'''
class Solution:
    inverse_pair = 0
    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(nums)
        return self.inverse_pair


    def mergeSort(self, alist):
        if len(alist) <= 1:
            return
    
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        self.mergeSort(lefthalf)
        self.mergeSort(righthalf)
    
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
                self.inverse_pair += (len(lefthalf) - i)
            k = k + 1
    
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
    
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1