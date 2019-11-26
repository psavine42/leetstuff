# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """https://leetcode.com/problems/merge-k-sorted-lists"""
    def mergeLists(self, lists) -> ListNode:
        lists = [x for x in lists if x]

        lists.sort(key=lambda x: x.val)
        head = None
        prev = None

        while lists:
            curr = lists.pop(0)
            new = ListNode(curr.val)
            if head:
                if prev:
                    prev.next = new
                    prev = new
                else:
                    prev = new
                    head.next = prev
            else:
                head = new

            curr = curr.next
            if curr is None:
                continue

            if len(lists) == 0:
                lists.append(curr)
                continue
            i = 0
            while i < len(lists) and lists[i].val < curr.val:
                i += 1
            lists.insert(i, curr)

        return head