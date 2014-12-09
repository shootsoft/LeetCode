# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):

        count = self.countNode(head)
        n = count - n

        if n == 0:
            head = head.next
            return head
        elif n < 0:
            return head

        c = head
        i = 1

        while i < n:
            i += 1
            c = c.next
        if c.next != None:
            c.next = c.next.next

        return head

    def countNode(self, head):

        if head == None:
            return 0
        else:
            return 1 + self.countNode(head.next)



class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None