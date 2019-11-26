from collections import defaultdict as ddict
from typing import List
from pprint import pprint


class Solution:
    """
    https://leetcode.com/problems/alien-dictionary/
    Runtime: 36 ms, faster than 80.31% of Python3 online submissions for Alien Dictionary.
    Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Alien Dictionary.
    """
    def topo_sort(self, letters, G):
        T = []

        letters = list(letters)
        N = len(letters)
        visited = [0]*N
        in_deg = [0]*N

        for i in range(N):
            for j in range(N):
                if letters[j] in G[letters[i]]:
                    in_deg[j] += 1

        q = []
        for i in range(N):
            if in_deg[i] == 0:
                q.append(i)
                visited[i] = 1

        while q:
            idx = q.pop()
            T.append(letters[idx])
            for j in range(N):
                if letters[j] in G[letters[idx]] and visited[j] == 0:
                    in_deg[j] -= 1
                    if in_deg[j] == 0:
                        q.append(j)
                        visited[j] = 1
        if sum(in_deg) > 0:
            return ''
        return ''.join(T)

    def alienOrder(self, words: List[str]) -> str:
        N = len(words)
        if N == 0:
            return ""
        if N == 1:
            return words[0]
        G = ddict(set)
        ls = set()
        for i in range(1, N):
            w1 = words[i - 1]

            w2 = words[i]
            ls.update(set(w1 + w2))

            j = 0
            l = min(len(w1), len(w2))
            while j < l:
                cprev = w1[j]
                cthis = w2[j]
                if cprev != cthis:
                    G[cprev].add(cthis)
                    break
                j += 1

        print(G)
        # traverse the graph
        return self.topo_sort(ls, G)


def run():
    tests = [
        [["wrt", "wrf", "er", "ett", "rftt"], "wertf"],
        [["wrt", "wrf", "er", "ett", "ewt", "rftt"], ""],
        [["z", "x", "z"], ""],
        # [["wrt", "wrf", "er", "ett", "rftta"], "wertfa"],
        [["wnlb"], "wnlb"],
        [["ri", "xz", "qxf", "jhsguaw", "dztqrbwbm", "dhdqfb", "jdv", "fcgfsilnb", "ooby"], ""],
        # [["wrt", "wrf", "er", "ett", "etw",  "rftt"], ""],

        # [["z","x"], 'zx'],


    ]
    s = Solution()
    for t, answer in tests:
        print(f'-----------------\n{t}\n--------------')
        res = s.alienOrder(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        assert res == answer


if __name__ == '__main__':
    run()

