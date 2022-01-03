# medium

'''2022-01-03'''
from typing import List

class Solution:
    mem = {0: [''], 1: ["()"]}
    def generateParenthesis(self, n: int) -> List[str]:
        if n in self.mem:
            return self.mem[n]
        pool = set()
        for a in range(0, n):  # ( seq of a "()"s ) seq of n-1-a "()"s
            l1 = self.generateParenthesis(a)
            l2 = self.generateParenthesis(n-1-a)
            for part_a in l1:
                for part_b in l2:
                    pool.add(f"({part_a}){part_b}")
        self.mem[n] = list(pool)
        return self.mem[n]
