from collections import Counter
from typing import List


class Solution:
    """
    https://leetcode.com/problems/minimum-domino-rotations-for-equal-row

    ----
    18:35 - 19:15 - fucking around trying a single loop.

    19:15-19:20 - Counter and done
    ---
    LESSON. KEEP IT SIMPLE STUPID.
     [ especially if its still O(N) ]

    Runtime: 1244 ms, faster than 87.87% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
    Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Minimum Domino Rotations For Equal Row.

    """
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        N = len(A)

        # ths most common element will be atleast 1/2 or the entries
        # if the dominos are split 50, 50, that is still fine
        X = Counter(A + B).most_common(1)[0][0]
        an, bn = 0, 0

        # run through arrays
        for i in range(N):
            ai, bi = A[i] == X, B[i] == X

            if ai and not bi:
                an += 1
            elif not ai and bi:
                bn += 1
            elif not ai and not bi:
                return -1

        return min(an, bn)