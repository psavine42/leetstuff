from typing import List

class Solution:
    """
    https://leetcode.com/problems/sliding-puzzle/
    Runtime: 36 ms, faster than 98.36% of Python3 online submissions for Sliding Puzzle.
    Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Sliding Puzzle.
    """
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = {0: [1, 3],
                 1: [0, 2, 4],
                 2: [1, 5],
                 3: [0, 4],
                 4: [5, 1, 3],
                 5: [2, 4],
                 }

        state = tuple(board[0] + board[1])
        zero = state.index(0)
        seen = set()
        solved = tuple([1, 2, 3, 4, 5, 0])

        q = [(state, zero), (None, None)]

        n_steps = 0
        while q:
            curr, z = q.pop(0)
            if curr is None:
                n_steps += 1
                if not q or q[0][0] is None:
                    return -1
                else:
                    q.append((None, None))
                    continue

            if curr == solved:
                return n_steps

            if curr in seen:
                continue

            seen.add(curr)
            for move in moves[z]:
                tmp = list(curr)
                tmp[z] = tmp[move]
                tmp[move] = 0
                next_state = tuple(tmp)
                q.append((next_state, move))

        return -1
