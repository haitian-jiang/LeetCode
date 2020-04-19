class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        if strs == []: # 输入为空则返回空串
            return output
        else:
            if len(strs) == 1: # 输入为一个词则返回该词
                return(strs[0])
            if "" in strs: # 输入中有空串则返回空串
                return "" # 以上是为了避免在else后的代码段中产生字符串索引越界错误
            else:
                for i in range(1, len(strs[0])+1):
                    new_output = strs[0][:i] # 尝试前i位
                    for j in range(len(strs)):
                        if strs[j][:i] != new_output: #如果有不同，就输出之前的
                            return output
                    output = new_output # 否则更新
                return output