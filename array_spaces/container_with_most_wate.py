from typing import List

class Solution:
    """
    https://leetcode.com/problems/container-with-most-water
    """
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        l, r = 0, N - 1
        w = N - 1

        mx_area = 0
        while w > 0:

            areaw = min(height[l], height[r]) * w
            mx_area = max(areaw, mx_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            w -= 1
        return mx_area

