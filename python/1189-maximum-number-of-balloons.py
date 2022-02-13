# easy
"""2022-02-13"""

from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = defaultdict(int)
        for c in text:
            count[c] += 1
        count['l'] //= 2
        count['o'] //= 2
        return min([count[i] for i in "balon"])