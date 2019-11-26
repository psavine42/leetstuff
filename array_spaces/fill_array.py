class Solution:
    """https://leetcode.com/problems/number-of-islands/

    """
    def numIslands(self, grid) -> int:
        N = len(grid)
        if N == 0:
            return 0
        M = len(grid[0])
        if M == 0:
            return 0

        isles = []
        ix2isle = {}

        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1":
                    exs = []
                    for (ni, nj) in [(i - 1, j), (i, j - 1)]:
                        if ni == -1 or nj == -1:
                            continue
                        if (ni, nj) in ix2isle:
                            exs.append((ni, nj))

                    if len(exs) == 1:
                        # one exists
                        indx = ix2isle[exs[0]]
                        ix2isle[(i, j)] = indx
                        isles[indx] += [(i, j)]

                    elif len(exs) == 2:
                        # merge
                        if ix2isle[exs[0]] != ix2isle[exs[1]]:
                            indx = ix2isle[exs[0]]
                            merge = isles[indx]

                            tgt = ix2isle[exs[1]]
                            isles[tgt].extend(merge)
                            for m in merge:
                                ix2isle[m] = tgt
                            isles[indx] = None

                        indx = ix2isle[exs[1]]
                        ix2isle[(i, j)] = indx
                        isles[indx] += [(i, j)]

                    else:
                        ix2isle[(i, j)] = len(isles)
                        isles.append([(i, j)])

        return len([x for x in isles if x])

def run():
    tests = [
        [[["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]], 1],
        [[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]], 1],
        [[["1","1","0","0","0"],["1","1","0","0","0"],["1","0","1","0","0"],["0","0","0","1","1"]], 3]
    ]
    s = Solution()
    for t, answer in tests:
        print(f'{t}---------------------')
        res = s.numIslands(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        # assert res == answer


if __name__ == '__main__':
    run()

