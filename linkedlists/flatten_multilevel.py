"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    """
    https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/submissions/
    """
    def flatten(self, head) :
        stack = []
        curr = head
        while curr or stack:

            # print(curr.val)
            if curr.child:

                nxt = curr.next
                child = curr.child
                if nxt:
                    nxt.prev = None
                    curr.next = None
                    stack.append(nxt)

                curr.child = None
                child.prev = curr
                curr.next = child
                curr = curr.next

            elif stack and not curr.next:
                nxt = stack.pop()
                nxt.prev = curr
                curr.next = nxt
                curr = curr.next

            elif curr.next:
                curr = curr.next

            elif not curr.next:
                break

        return head