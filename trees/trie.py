from string import ascii_lowercase
from typing import List
from collections import defaultdict as ddict

class TrieNode:
    def __init__(self):
        self.childs = [None] * 26
        self.is_leaf = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        i, n = 0, len(word)

        while i < n:
            chr_idx = ord(word[i]) - 97
            if node.childs[chr_idx] is None:
                node.childs[chr_idx] = TrieNode()
            node = node.childs[chr_idx]
            i += 1

        node.is_leaf = True

    def __contains__(self, word):
        """ doe the word exist in self ?"""
        node = self.root
        i, n = 0, len(word)

        while i < n:
            chr_idx = ord(word[i]) - 97
            if node.childs[chr_idx] is None:
                return False
            node = node.childs[chr_idx]
            i += 1

        return node.is_leaf

    def search(self, word):
        return word in self

    def startsWith(self, pref):
        node = self.root
        i, n = 0, len(pref)

        while i < n:
            chr_idx = ord(pref[i]) - 97
            if node.childs[chr_idx] is None:
                return False
            node = node.childs[chr_idx]
            i += 1
        return True

    def word_or_pre(self, pref):
        """
        -1 -> if prefix doesnt exist
        0  -> if prefix exists
        1  -> word exists
        """
        node = self.root
        i, n = 0, len(pref)

        while i < n:
            chr_idx = ord(pref[i]) - 97
            if node.childs[chr_idx] is None:
                return -1
            node = node.childs[chr_idx]
            i += 1

        return node.is_leaf

    def word_root(self, pref):
        """
        https://leetcode.com/problems/replace-words
        """
        node = self.root
        i, n = 0, len(pref)
        res = ''
        while i < n:
            chr_idx = ord(pref[i]) - 97
            if node.childs[chr_idx] is None:
                return pref

            res += pref[i]
            if node.childs[chr_idx].is_leaf is True:
                return res

            node = node.childs[chr_idx]
            i += 1

        if node.is_leaf is True:
            return res
        return ''


class Solution:
    """https://leetcode.com/problems/word-search-ii/"""
    def __init__(self):
        self.tree = Trie()
        self.N = None
        self.M = None

    def dfs(self, w):
        pass

    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(board)
        M = len(board[0])
        w = len(word) - 1

        for a, b in [(i, j) for i in range(N) for j in range(M)]:
            seen = ddict(set)
            q = [(a, b, 0)]
            while q:

                ni, nj, char_ix = q.pop()
                if word[char_ix] != board[ni][nj]:
                    continue

                chk = seen.get((ni, nj), set())
                if chk is not None and chk != char_ix:
                    continue

                seen[(ni, nj)] = char_ix
                if char_ix == w:
                    return True

                for xi, xj in [[ni + 1, nj], [ni - 1, nj],
                               [ni, nj + 1], [ni, nj - 1]]:
                    if 0 <= xi <= N - 1 and 0 <= xj <= M - 1:
                        if word[char_ix + 1] == board[xi][xj]:
                            q.append((xi, xj, char_ix + 1))
        return False

    def findWords(self, board, words):
        for word in words:
            self.tree.insert(word)

        self.N = len(board)
        self.M = len(board[0])
        letter_front = []
        q = [(0, 0, )]
        while q:
            ni, nj = q.pop()
            for i, j in [[ni + 1, nj], [ni - 1, nj],
                         [ni, nj + 1], [ni, nj - 1]]:
                if 0 <= i <= N - 1 and 0 <= j <= M - 1:
                    pass
        return


def run1():
    board = [
        [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ],
        [
            ["C", "A", "A"],
            ["A", "A", "A"],
            ["B", "C", "D"]],
        [["A", "B", "C", "E"],
         ["S", "F", "E", "S"],
         ["A", "D", "E", "E"]]


    ]
    words = [
        ["ABCCED", "SEE", "ABCB"],
        ["AAB"],
        ["ABCESEEEFS"]
    ]

    res = [
        [True, True, False ],
        [True],
        [True]
    ]

    s = Solution()
    for b, ws, answers in zip(board, words, res):
        for w, answer in zip(ws, answers):
            print(f'-------------------------------')
            print(w)
            res = s.exist(b, w)
            print(f'\n{str(w)} --> {res}, {answer}, {res == answer}')
            assert res == answer


def run():
    board = [
        [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
        ]
    ]
    words = [["oath", "pea", "eat", "rain"]]

    res = [ ["eat","oath"] ]
    s = Solution()
    for b, w, answer in zip(board, words, res):
        print(f'-------------------------------')
        res = s.findWords(b, w)
        print(f'\n{str(w)} --> {res}, {answer}, {res == answer}')
        assert res == answer


if __name__ == '__main__':
    run1()

