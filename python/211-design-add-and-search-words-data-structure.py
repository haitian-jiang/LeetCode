# 2022-01-15
'''medium'''

class WordDictionary:

    def __init__(self):
        self.is_end = False
        self.next = [None] * 26

    def addWord(self, word: str) -> None:
        node = self
        for ch in word:
            order = ord(ch)-ord('a')
            if node.next[order] is None:
                node.next[order] = WordDictionary()
            node = node.next[order]
        node.is_end = True

    def search(self, word: str) -> bool:
        ch = word[0]
        order = ord(ch)-ord('a')
        if len(word) == 1:
            if ch == ".":
                for nxt in self.next:
                    if nxt and nxt.is_end: 
                        return True
            else:
                if self.next[order] and self.next[order].is_end:
                    return True
            return False

        if ch != '.':
            if self.next[order] is None:
                return False
            else:
                return self.next[order].search(word[1:])
        else:
            for nxt in self.next:
                if nxt is not None:
                    if nxt.search(word[1:]) == True:
                        return True
            return False
