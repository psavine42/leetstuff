from typing import List

class Solution:
    """
    https://leetcode.com/problems/sliding-puzzle/
    Runtime: 36 ms, faster than 98.36% of Python3 online submissions for Sliding Puzzle.
    Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Sliding Puzzle.
    """
    def maxCoins(self, nums: List[int]) -> int:


        dp =

        nums.sort()

        return -1


def run():
    tests = [
        [[3, 1, 5, 8], 167 ]

    ]
    s = Solution()
    for t, answer in tests:
        print(f'-----------------\n{t}\n--------------')
        res = s.maxCoins(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        assert res == answer


if __name__ == '__main__':
    run()

