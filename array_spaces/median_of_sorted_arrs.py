from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n, m = len(nums1), len(nums2)
        t = n + m
        odd = 1 if t % 2 == 1 else 0

        merge_till = t // 2

        new = []
        i = 0
        while i <= merge_till and (nums1 or nums2):
            if not nums1:
                new.append(nums2.pop(0))

            elif not nums2:
                new.append(nums1.pop(0))

            elif nums1[0] > nums2[0]:
                new.append(nums2.pop(0))
            else:
                new.append(nums1.pop(0))
            i += 1

        # print(new)
        if odd == 1:
            return float(new[-1])
        else:
            return (new[-2] + new[-1]) / 2


def run():
    tests = [
        [
            [1, 3],
            [],
            2
        ],

        [
            [1],
            [],
            1
        ],

    ]
    s = Solution()
    for t, t2, answer in tests:
        print(f'-----------------\n{t}\n--------------')
        res = s.findMedianSortedArrays(t, t2)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        assert res == answer


if __name__ == '__main__':
    run()

