# easy
class Solution: # 通过循环，先看前两位，如果不特殊看第一位，将值加上后抛去加过的前一/两位(采用切片)
    def romanToInt(self, s: str) -> int:
        ans = 0
        while(s):
            if len(s) > 1:
                if (s[0],s[1]) == ("I","V"):
                    ans += 4
                    s = s[2:]
                    continue
                elif (s[0],s[1]) == ("I","X"):
                    ans += 9
                    s = s[2:]
                    continue
                elif (s[0],s[1]) == ("X","L"):
                    ans += 40
                    s = s[2:]
                    continue
                elif (s[0],s[1]) == ("X","C"):
                    ans += 90
                    s = s[2:]
                    continue
                elif (s[0],s[1]) == ("C","D"):
                    ans += 400
                    s = s[2:]
                    continue
                elif (s[0],s[1]) == ("C","M"):
                    ans += 900
                    s = s[2:]
                    continue
            if s[0] == "I":
                ans += 1
                s = s[1:]
                continue
            elif s[0] == "V":
                ans += 5
                s = s[1:]
                continue
            elif s[0] == "X":
                ans += 10
                s = s[1:]
                continue
            elif s[0] == "L":
                ans += 50
                s = s[1:]
                continue
            elif s[0] == "C":
                ans += 100
                s = s[1:]
                continue
            elif s[0] == "D":
                ans += 500
                s = s[1:]
                continue
            elif s[0] == "M":
                ans += 1000
                s = s[1:]
                continue
        return ans