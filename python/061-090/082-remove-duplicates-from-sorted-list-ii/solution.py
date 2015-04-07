__author__ = 'yinjun'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):

        h = ListNode(0)
        h.next = head

        c = h
        a = h.next

        if a == None or a.next == None:
            return h.next

        b = a.next

        while b != None:

            find = a.val == b.val
            while b!=None and a.val == b.val:
                b = b.next
            if find:
                c.next = b
                a = b

                if b!=None:
                    b = b.next
            else:
                c = a
                a = a.next
                b = a.next

        return h.next

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None