class Solution: # 递归算法
    def countAndSay(self, n: int) -> str:
        if n == 1: # 递归出口
            return "1"
        laststr = self.countAndSay(n - 1)
        laststr = list(laststr)
        ans_list = []
        while (laststr): # 通过计数器数数量，数一次弹出一个
            counter = 0
            cur_val = laststr[0]
            while (laststr != [] and laststr[0] == cur_val): # 判断不空防止索引出错
                laststr.pop(0)
                counter += 1
            ans_list.append(str(counter))
            ans_list.append(cur_val)
        return "".join(ans_list)