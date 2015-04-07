__author__ = 'yinjun'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):

        h1 = ListNode(0)
        h2 = ListNode(0)

        h1h = h1
        h2h = h2

        h = head

        while h != None:

            if h.val < x :
                h1.next = ListNode(h.val)
                h1 = h1.next
            else:
                h2.next = ListNode(h.val)
                h2 = h2.next

            h = h.next

        h1.next = h2h.next

        return h1h.next
