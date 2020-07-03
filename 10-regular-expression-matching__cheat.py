# hard
import re # 作弊方法
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if re.match(p+'$',s) == None: # match从头开始匹配，不一定匹配到尾，要加$表示结尾
            return False
        return True