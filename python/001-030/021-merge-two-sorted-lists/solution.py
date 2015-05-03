# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):

        head = None

        if l1 == None:
            head = l2
            return head
        elif l2==None:
            head = l1
            return head

        h1 = l1
        h2 = l2
        head = ListNode(0);
        h = head

        pre = None
        while h1!=None and h2!=None:
            if h1.val<h2.val:
                h.next = h1
                h = h.next
                h1 = h1.next
            else:
                h.next = h2
                h = h.next
                h2 = h2.next

        if h1==None and h2!=None:
            h.next = h2
        elif h1!=None and h2==None:
            h.next = h1

        return head.next