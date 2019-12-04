from collections import defaultdict as ddict
from typing import List
from pprint import pprint


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        N = len(matrix)
        if N == 0:
            return []

        M = len(matrix[0])
        if M == 0:
            return []

        update_by = [-1, -1, 1, 1]
        bounds = [M - 1, N - 1, 0, 1]
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        di = 0
        active_bnd = 1
        ij = [0, -1]
        for _ in range(N * M):
            ij = [ij[0] + dirs[di][0], ij[1] + dirs[di][1]]

            i, j = ij
            res.append(matrix[i][j])

            if ij[active_bnd] == bounds[di]:

                bounds[di] += update_by[di]
                di = di + 1 if di < 3 else 0
                active_bnd = not active_bnd

        return res


def run():
    tests = [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ],
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
    ]
    res = [
        [1, 2, 3, 6, 9, 8, 7, 4, 5],
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        [1, 2, 3, 4, 8, 8, 12, 11, 10, 9, 5, 5, 6, 7, 7, 6]
    ]
    s = Solution()
    for t, answer in zip(tests, res):
        print(f'-----------------\n{t}\n--------------')
        res = s.spiralOrder(t)
        print(f'\n{t} --> \n{res}\n{answer}, {res == answer}')
        assert res == answer


if __name__ == '__main__':
    run()

