import numpy as np
from typing import List


class Solution:
    def step(self, idxs):
        """ create a list of stuff to drop """
        cols = idxs[:, 1]

        return

    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        N, M = len(board), len(board[0])
        game = np.asarray(board, dtype=int)

        locs = [[[0, 0]]]
        candidates = []

        while locs:
            loc = locs.pop()
            i, j = loc[-1]
            v = game[i, j]

            for ai, aj in [[i, j + 1], [i + 1, j]]:
                if ai == N or aj == M:
                    continue
                if game[ai, aj] == v:


        # step
        return



def run():
    tests = [
        [[[110,5,112,113,114],[210,211,5,213,214],
          [310,311,3,313,314],[410,411,412,5,414],
          [5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],
          [810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]],

         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0], [110, 0, 0, 0, 114], [210, 0, 0, 0, 214],
          [310, 0, 0, 113, 314], [410, 0, 0, 213, 414],
          [610, 211, 112, 313, 614], [710, 311, 412, 613, 714],
          [810, 411, 512, 713, 1014]]

         ]
    ]
    s = Solution()
    for t in tests:
        print(f'-----------------\n{t}\n--------------')
        res = s.solveSudoku(t)
        print(f'\n{t} --> {res}, ')
        # assert res == answer


if __name__ == '__main__':
    run()

