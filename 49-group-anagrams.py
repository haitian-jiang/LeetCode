# medium

from typing import List

'''2020-07-17'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nums = list(map(lambda x:''.join(sorted(list(x))), strs))  # 将每个字符串排序
        ind_dict = {}  # {'aet': [0, 1, 3], ...}, key为排好序的字符串，value为值为此字符串的下标所组成的列表
        for i in range(len(nums)):
            if nums[i] not in nums[:i]:  # 如果次单词第一次出现，加入字典中，并初始化列表
                ind_dict[nums[i]] = [i]
            else:  # 不是第一次出现，把下标加入列表
                ind_dict[nums[i]].append(i)
        ans_list = []  # 根据字典中的下标列表生成答案
        for ind in ind_dict.values():
            ans_list.append(list(map(lambda x:strs[x], ind)))
        return ans_list

