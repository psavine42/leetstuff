from typing import List
import itertools

class Solution:
    """
    https://leetcode.com/problems/game-of-life
    """
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = len(board)
        if N == 0:
            return
        M = len(board[0])
        if M == 0:
            return

        def is_alive(n_or_q):
            return n_or_q if isinstance(n_or_q, int) else n_or_q[0]

        adders = list(itertools.permutations([1, -1, 0], 2)) + [[1, 1], [-1, -1]]
        # print(adders)
        update = []
        for i in range(N):
            for j in range(M):

                # num_dead = 0
                num_alive = 0
                alive = is_alive(board[i][j])

                for ai, aj in adders:
                    aii = i + ai
                    ajj = j + aj
                    if not (0 <= aii < N):
                        continue
                    if not (0 <= ajj < M):
                        continue
                    num_alive += is_alive(board[aii][ajj])

                # logic
                if alive == 1 and num_alive in (2, 3):
                    nxt_state = 1
                elif alive == 0 and num_alive == 3:
                    nxt_state = 1
                else:
                    nxt_state = 0

                board[i][j] = [alive, nxt_state]

        for i in range(N):
            for j in range(M):
                board[i][j] = board[i][j].pop()
