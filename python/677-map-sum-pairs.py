# medium
'''2022-01-15'''

class MapSum:

    def __init__(self):
        self.is_end = False
        self.children = defaultdict(MapSum)
        self.val = None

    def insert(self, key: str, val: int) -> None:
        node = self
        for ch in key:
            node = node.children[ch]
        node.val = val
        node.is_end = True

    def _sum(self) -> int:
        if len(self.children) == 0:
            return self.val if self.val else 0
        
        total = 0
        if self.val is not None:
            total += self.val
        for nxt in self.children.values():
            total += nxt._sum()
        return total

    def sum(self, prefix: str) -> int:
        node = self
        for ch in prefix:
            node = node.children[ch]
        return node._sum()
