# easy
'''2022-01-14'''

from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destinations = defaultdict(bool)
        for path in paths:
            destinations[path[0]] = True
            destinations[path[1]] = destinations[path[1]]
        for destination in destinations:
            if not destinations[destination]:
                return destination
