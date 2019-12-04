from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[int]]):
        N = len(matrix)
        if N == 0:
            return 0
        M = len(matrix[0])
        if M == 0:
            return 0

        for i in range(N):
            for j in range(M):
                matrix[i][j] = int(matrix[i][j])

        for i in range(1, N):
            for j in range(M):
                matrix[i][j] += int(matrix[i-1][j])

        [print(x) for x in matrix]

        maxA = 0

    def v2(self, matrix):
        """

        h(0, c) = 0
        h(r, c) = 0 if matrix[r][c] == 0
        h(r, c) = h(r-1, c)+1 otherwise

        l(r, 0) = 0
        l(r, c) = c-p if matrix[r-1][c] == 0
        l(r, c) = min(l(r − 1, c), c − p) otherwise

        r(r,C+1) = 0
        r(r,c) = p-c if matrix[r-1][c] == 0
        r(r,c) = min(r(r − 1, c), p − c) otherwise
        """
        import numpy as np
        mat = np.asarray(matrix, dtype=int)
        m2 = np.asarray(matrix, dtype=int)
        N, M = mat.shape
        print(mat)
        h = np.zeros((N+1, M+1), dtype=int)
        l = np.zeros((N+1, M+1), dtype=int)
        r = np.zeros((N+1, M+1), dtype=int)

        for i in range(N):
            for j in range(M):
                if mat[i, j] == 1:
                    h[i, j] = h[i - 1, j] + 1
                    l[i, j] = l[i, j - 1] + 1

        for i in reversed(range(N)):
            for j in reversed(range(M)):
                if mat[i, j] == 1:
                    r[i, j] = r[i, j + 1] + 1

        for m in [l, r, h]:
            print()
            print(m)

        maxA = 0
        for i in range(N):
            for j in range(M):
                v = h[i+1, j+1] * l[i+1, j+1]
                m2[i, j] = v
                maxA = max(v, maxA)
        print()
        print(m2)
        return maxA

    def v3(self, matrix):
        """

        h(0, c) = 0
        h(r, c) = 0 if matrix[r][c] == 0
        h(r, c) = h(r-1, c)+1 otherwise

        l(r, 0) = 0
        l(r, c) = c-p if matrix[r-1][c] == 0
        l(r, c) = min(l(r − 1, c), c − p) otherwise

        r(r,C+1) = 0
        r(r,c) = p-c if matrix[r-1][c] == 0
        r(r,c) = min(r(r − 1, c), p − c) otherwise
        """
        import numpy as np
        mat = np.asarray(matrix, dtype=int)
        m2 = np.asarray(matrix, dtype=int)
        N, M = mat.shape
        print(mat)
        h = np.zeros((N+1, M+1), dtype=int)
        l = np.zeros((N+1, M+1), dtype=int)
        r = np.zeros((N+1, M+1), dtype=int)
        import collections
        q = collections.deque()

        curr = None
        for j in range(M):
            if mat[0, j] == 1 and curr is None:
                curr = j
            elif mat[0, j] == 0 and curr is not None:
                q.append((0, curr, 1, j))
                curr = None

        print(q)

        while q:
            rng = q.popleft()
            # try expand down


            # try expand right


        return maxA



def run():
    tests = [
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ],
        [
            ["1", "1", "1", "0", "0"],
            ["1", "1", "1", "1", "1"],
            ["0", "0", "1", "1", "1"],
            ["1", "1", "0", "1", "0"]
        ]
    ]

    tfts = [6, 6]
    s = Solution()
    for t, answer in zip(tests, tfts):
        print(f'-------------------------------')
        res = s.v3(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        assert res == answer


if __name__ == '__main__':
    run()




