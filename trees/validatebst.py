class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    tts = 15 minutes ??
    https://leetcode.com/problems/validate-binary-search-tree
    """
    def isValidBST(self, root: TreeNode) -> bool:
        """


        :param root:
        :return:
        """
        if not root:
            return True
        q = [(root, None, None)]

        while q:
            el, lb, ub = q.pop()
            if lb is not None and el.val <= lb:
                return False

            if ub is not None and el.val >= ub:
                return False

            if el.left:
                q.append((el.left, lb, el.val))

            if el.right:
                q.append((el.right, el.val, ub))

        return True


