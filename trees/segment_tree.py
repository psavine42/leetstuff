from typing import List


class SegmentTreeNode:
    def __init__(self, s, e, sum=0):
        self.start = s
        self.end = e
        self.sum = sum


class NumArray:
    def __init__(self, nums: List[int]):
        end = len(nums) - 1
        self.root = None
        if end > 0:
            self.root = self.build(nums, 0, end)

    def build(self, nums, start, end):
        if start > end:
            return None
        root = SegmentTreeNode(start, end, 0)
        if start == end:
            root.sum = nums[start]

        else:
            mid = start + (end - start) // 2
            root.left = self.build(nums, start, mid)
            root.right = self.build(nums, mid + 1, end)
            root.sum += root.left.sum if root.left else 0
            root.sum += root.right.sum if root.right else 0

        return root

    def update(self, index, val):
        self._update(self.root, index, val)

    def _update(self, node, index, val):
        if node is None:
            return
        if node.end == node.start and index == node.end:
            node.sum = val

        mid = node.start + (node.end - node.start) // 2
        if index <= mid:
            self._update(node.left, index, val)

        else:
            self._update(node.right, index, val)

        node.sum = 0
        node.sum += node.left.sum if node.left else 0
        node.sum += node.right.sum if node.right else 0

    def _get_sum(self, node, start, end):
        if node is None:
            return 0

        # node is inside the range
        if start <= node.start and end >= node.end:
            return node.sum

        mid = start + (end - start) // 2

        total = 0

        if end < mid:
            # range is strictly to the left
            total += self._get_sum(node.left, start, end)
        elif start > mid:
            # range is strictly to the right
            total += self._get_sum(node.right, start, end)
        else:
            #
            total += self._get_sum(node.left, start, mid)
            total += self._get_sum(node.right, mid+1, end)

        return total

    def sumRange(self, i, j):
        if i == self.root.start and j == self.root.end:
            return self.root.sum
        return self._get_sum(self.root, i, j)


def lsb(x :int) -> int:
    # return bin(x)[2:].index('1')
    return x & -x


class BIT:
    def __init__(self, nums):
        self._nums = nums
        self._size = len(nums) + 1 # root is index 0
        self._bit = [0]*self._size
        for i in range(1, self._size):
            self._add(i, nums[i-1])

    def __repr__(self):
        s = f'{self._bit}'
        return s

    def _sum(self, i):
        ttl = 0
        while i > 0:

            ttl += self._bit[i]
            i -= lsb(i)
        return ttl

    def _add(self, i, k):
        """
        who owns the index?
        x ,  { y }
        1 ->
        2 -> [3]
        4 -> [5, 6, 7]
        8 ....

        Bit(y) -> x

        """
        while i < self._size:
            self._bit[i] += k
            i += lsb(i)

    def __len__(self):
        return self._size - 1

    # public api --------------------------------------------
    def tolist(self):
        res = []
        prev = 0
        for i in range(1, self._size):
            this = self._sum(i)
            val = this - prev
            res.append(val)
            prev = this
        return res

    def append(self, val):
        self._size += 1
        self._bit.append(0)
        self._add(self._size-1, val)

    def update(self, i, val):
        """ """
        curr = self._sum(i+1) - self._sum(i)
        print(curr)
        self._add(i+1, val - curr)

    def sumRange(self, i, j) -> int:
        """ """
        return self._sum(j+1) - self._sum(i)


def run():
    """ inclusive last index

        [1, 3, 5]

         9
        / \

    """
    tests = [
        # [
        #     ["", "sumRange", "sumRange",  "sumRange", "update", "sumRange", "sumRange", "sumRange"],
        #     [[1, 2, 3, 4, 5], [0, 2], [1, 2], [1, 3], [1, 3], [0, 2], [1, 2], [0, 1]]
        # ],
        [
            ["NumArray", "sumRange", "update", "sumRange"],
            [[-1], [0, 0], [0, 1], [0, 0]]
        ]
    ]

    results = [
        # [None, 3, 2, 5, None, 4, 2, 2],
        [None, -1, None, 1],

    ]
    for test, res in zip(tests, results):
        print('-----'*20)
        cmds, params = test
        cmds.pop(0)
        p = params.pop(0)
        res.pop(0)
        obj = BIT(p)
        for cmd, param, exp in zip(cmds, params, res):
            v = getattr(obj, cmd)(*param)
            print(obj)
            print(f'------\n{cmd}, {param} --> {v} : {exp}')
            assert exp == v


if __name__ == '__main__':
    run()










