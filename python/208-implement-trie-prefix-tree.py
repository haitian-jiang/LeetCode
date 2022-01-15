# medium
'''2022-01-15'''

class Trie:

    def __init__(self):
        self.is_end = False
        self.next = [None] * 26

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            order = ord(ch)-ord('a')
            if node.next[order] is None:
                node.next[order] = Trie()
            node = node.next[order]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            order = ord(ch)-ord('a')
            if node.next[order] is None:
                return False
            node = node.next[order]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            order = ord(ch)-ord('a')
            if node.next[order] is None:
                return False
            node = node.next[order]
        return True
