from typing import List


class Solution:

    def jump(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/jump-game-ii/
        """
        l = len(nums) - 1
        curr_i = 0
        jumps = 0

        while curr_i < l and jumps < l:

            # print(f'base {curr_i} / {l} -> {nums[curr_i]}')

            if nums[curr_i] + curr_i >= l:
                return jumps + 1

            best1, best_j = 0, 0
            for j in range(1, nums[curr_i]+1):

                if curr_i + j > l:
                    return jumps + 1

                if nums[curr_i + j] + j > best1:
                    best1 = nums[curr_i + j] + j
                    best_j = j

            if best_j == 0:
                return False

            # print(f'nj={jumps} i={curr_i}, j0={best_j} ', )
            #
            curr_i += best_j
            # print(curr_i)
            jumps += 1
        return jumps

    def canJump(self, nums):
        """
        https://leetcode.com/problems/jump-game/
        """
        return self.jump(nums) is not False


def canjump():
    tests = [
        [[3,2,1,0,4], False],
        [[2, 3, 1, 1, 4], True],
        [[0, 1, 2], False],
        [[2, 1, 0], True],
    ]
    s = Solution()
    for t, answer in tests:
        print(f'-----------------\n{t}\n--------------')
        res = s.canJump(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        assert res == answer


def jump():
    tests = [
        [[2, 3, 1, 1, 4], 2],
        [[2, 3, 0, 1, 4], 2],
        [[2, 3, 1], 1],
        [[1, 3, 2], 2],

        [[3, 2, 1, 1, 4, 5, 6, 1, 0, 4], 4],
        [[3, 2, 1], 1],
        [[4, 1, 1, 3, 1, 1, 1], 2]

    ]
    s = Solution()
    for t, answer in tests:
        print(f'-----------------\n{t}\n--------------')
        res = s.jump(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        assert res == answer


if __name__ == '__main__':
    canjump()

