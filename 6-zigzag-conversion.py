# medium
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        all_list=[]  # contains lists, each list is a row
        for _ in range(numRows):  # initialize all_list
            all_list.append([])
        mod = 2 * (numRows - 1)  # the number of differnt positions
        if mod == 0:  # the case that len(s) is 1 while numRows is 1
            return s  # then the answer should be s itself
        for str_ind in range(len(s)):  # for each char, find its row
            remainder = str_ind % mod  # the remainder determines which row to be in
            if remainder < numRows:  # in this case, char lies in the vertical bar
                all_list[remainder].append(s[str_ind])
            else:  # char lies in the slash
                all_list[mod-remainder].append(s[str_ind])
        for i in range(len(all_list)):  # convert each list to string
            all_list[i] = ''.join(all_list[i])
        return ''.join(all_list)  # convert the answer list to string
