# easy
'''2022-01-09'''

from collections import defaultdict
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        for i in range(len(releaseTimes)-1, 0, -1):
            releaseTimes[i] = releaseTimes[i] - releaseTimes[i-1]
        time = 0
        key = ''
        for i in range(len(releaseTimes)):
            time, key = max((time, key), (releaseTimes[i], keysPressed[i]))
        return key
