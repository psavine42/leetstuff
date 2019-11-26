# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """https://leetcode.com/problems/count-complete-tree-nodes"""
    def countNodes(self, root) -> int:
        T = 0
        q = [root]
        while q:
            el = q.pop()
            if el is None:
                continue

            T += 1

            q.append(el.right)
            q.append(el.left)
        return T


def run():
    tests = {

    }
    s = Solution()
    for t, answer in tests.items():
        print(f'{t}---------------------')
        res = s.countOfAtoms(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        # assert res == answer


if __name__ == '__main__':
    run()

