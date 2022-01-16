# hard
'''2022-01-16'''

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        found_words = []
        words = set(words)

        def dfs(r, c, l, w):
            if l > 10:
                return
            if w in words:
                found_words.append(w)
                words.remove(w)
            mem = board[r][c]
            board[r][c] = ''
            for r_, c_ in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= r_ < len(board) and 0 <= c_ < len(board[0]) and board[r_][c_]:
                    dfs(r_, c_, l+1, w+board[r_][c_])
            board[r][c] = mem


        for i in range(len(board)):
            for j in range(len(board[0])):
                if len(words) == 0:
                    return found_words
                start = board[i][j]
                dfs(i, j, 1, start)

        return found_words


from collections import defaultdict

class Trie:
    def __init__(self):
        self.word = ""
        self.children = defaultdict(Trie)

    def insert(self, word):
        node = self
        for ch in word:
            node = node.children[ch]
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        found_words = []
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(r, c, node):
            if board[r][c] not in node.children:
                return
            w = board[r][c]
            nxt = node.children[w]
            if nxt.word:
                found_words.append(nxt.word)
                nxt.word = ""
            if len(nxt.children):
                board[r][c] = ""
                for r_, c_ in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if 0 <= r_ < len(board) and 0 <= c_ < len(board[0]) and board[r_][c_] in nxt.children:
                        dfs(r_, c_, nxt)
                board[r][c] = w
            if not nxt.children:
                node.children.pop(w)



        for i in range(len(board)):
            for j in range(len(board[0])):
                start = board[i][j]
                dfs(i, j, trie)

        return found_words

