# easy
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        if numRows == 0: # 题目中强调非负整数
            return ans
        for i in range(numRows): # 最左侧的1
            ans.append([1])
        if numRows == 1: # 防止动归时-1越界
            return ans
        for i in range(1,numRows):
            for j in range(1,len(ans[i-1])):
                ans[i].append(ans[i-1][j-1]+ans[i-1][j])
            ans[i].append(1) # 右侧的1
        return ans