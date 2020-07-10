# medium
'''2020-07-11'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or '1' in digits:
            return []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        words = list(mapping[digits[0]])  # 放入第一个数对应的字母
        digits = digits[1:]  # 弹出第一个数
        while digits:  # 还没有弹完
            new_words = []
            for char in mapping[digits[0]]:  # 把每个字母都加到words中每个元素的末位，把这几个列表组合成一个，变成新的words
                new_words += list(map(lambda s: s+char, words))
            words = new_words  # 更新
            digits = digits[1:]
        return words
