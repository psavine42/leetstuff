from typing import List
from collections import defaultdict as ddict


class Solution:
    def __init__(self):
        self.opts = ddict(set)
        self.solved = {}
        # self.board = None
        self.constr = {}  # [[set() for j in range(3)] for i in range(3)]

    def backtrack(self, board, opts):
        # opts = self.opts[(i, j)]
        i, j = self.get_best_ij(opts)
        opts = opts[(i, j)]
        for k, num in enumerate(opts):
            this = opts[k:]
            board[i][j] = num
            if self.backtrack(board, opts) is True:
                return True

            board[i][j] = 0


    def check_safe(self, board, i,j, val):


    def elimination_step(self, board, opts):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 1:
                    continue
                opts = self.opts[(i, j)]

                for ci, cj in self.constr[(i, j)]:
                    if board[ci][cj]:
                        opts.difference_update({board[ci][cj]})
                self.opts[(i, j)] = opts
                if len(opts) == 1:
                    v = list(opts)[0]
                    self.solved[(i, j)] = v
                    board[i][j] = v

    def stat(self):
        num_opt = 0
        num_solv = 0
        for k,v in self.opts.items():
            if len(v) == 1:
                num_solv += 1
            else:
                num_opt += len(v)
        print(num_solv, num_opt)

    def get_best_ij(self, opts):
        best, ij = 10, None
        for k, v in opts.items():
            if len(v) < best:
                best, ij = len(v), k
        return ij[0], ij[1]

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # s# elf.board = [x[:] for x in board]
        for i in range(9):
            for j in range(9):
                bij = board[i][j]
                if bij == 0:
                    self.opts[(i, j)] = set(range(1, 10))
                else:
                    self.opts[(i, j)].add(int(bij))
                    self.solved[(i, j)] = int(bij)

                si, sj = 3 * (i // 3), 3 * (j // 3)
                rows = set([(i, x) for x in range(9) if x != j])
                cols = set([(x, j) for x in range(9) if x != i])
                squares = set([(x+si, y+sj) for x in range(3) for y in range(3)
                                       if x+si != i and y+sj != j])

                self.constr[(i, j)] = set.union(*[rows, cols, squares])
                print((i, j), self.constr[(i, j)])

        self.stat()
        self.elimination_step(board)
        self.stat()








def run():
    tests = [
        [[5, 3, 0,   0, 7, 0,  0, 0, 0],
         [6, 0, 0,   1, 9, 5,     0, 0, 0],
         [0, 9, 8,   0,0,0,   0, 6, 0],

         [8, 0,0,   0, 6, 0,   0, 0, 3],
         [4, 0,0,   8, 0, 3,   0,0, 1],
         [7, 0,0,   0, 2, 0,   0, 0, 6],

         [0, 6, 0,  0, 0, 0, 2, 8, 0],
         [0, 0, 0,  4, 1 ,9,      0, 0, 5],
         [0, 0, 0,  0, 8, 0, 0, 7, 9],
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

