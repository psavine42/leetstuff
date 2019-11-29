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
            mid = start - (end - start) // 2
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

        mid = node.start - (node.end - node.start) // 2
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

        mid = start - (end - start) // 2

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
