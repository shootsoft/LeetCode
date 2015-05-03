# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):

        c = head

        if c == None or c.next == None:
            return head


        p = ListNode(0)
        head = p

        while c != None and c.next!=None:
            p.next = c.next
            n = c.next
            c.next = n.next
            n.next = c
            p = c
            c = c.next
            #ListNode.output(c)

        return head.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def create(list):
        lic = len(list)
        head = ListNode(0)
        n = head
        for j in range(lic):
            n.next = ListNode(list[j])
            n = n.next
        #ListNode.output(head)
        return head.next


    @staticmethod
    def create_lists(lists):
        l = []
        c = len(lists)
        for i in range(c):
            li = list(lists[i])
            l.append(ListNode.create(li))
        return l

    @staticmethod
    def output(n):
        b = n
        print '[',
        while b != None:
            print b.val,
            b = b.next
        print ']'




s = Solution()

ListNode.output( s.swapPairs( ListNode.create([1,2,3,4]) ) )
#ListNode.output( s.swapPairs( ListNode.create([1,2]) ) )