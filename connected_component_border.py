from typing import List


class Solution:
    """https://leetcode.com/problems/coloring-a-border/submissions/

    Runtime: 140 ms, faster than 91.83% of Python3 online submissions for Coloring A Border.
    Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Coloring A Border.
    """
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:

        N, M = len(grid), len(grid[0])
        seen = set()
        edge = set()
        C = grid[r0][c0]
        q = [(r0, c0)]
        while q:
            x, y = q.pop()

            if (x, y) in seen:
                continue
            seen.add((x, y))

            on_edge = True if x == 0 or x == N - 1 or y == 0 or y == M - 1 else False
            for (nx, ny) in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if nx < 0 or nx == N or ny < 0 or ny == M:
                    # onedge += 1
                    continue
                if grid[nx][ny] == C:
                    if (nx, ny) not in seen:
                        q.append((nx, ny))
                else:
                    on_edge = True
            # print(x,y, on_edge)
            if on_edge is True:
                edge.add((x, y))

        for (nx, ny) in edge:
            grid[nx][ny] = color
        return grid

