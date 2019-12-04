# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """https://leetcode.com/problems/recover-binary-search-tree/"""
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        q = [(root, root.val, root.val)]

        while q:
            node, lb, rb = q.pop(0)
            # left
            if node.left:
                if node.left.val > lb:
                # found 1
                else:
                    q.append((node.left, lb, node.val))

            if node.right:
                if node.right.val < rb:
                # found 1
                else:
                    q.append((node.left, node.val, rb))

