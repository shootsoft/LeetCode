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


ListNode.output(s.mergeTwoLists(ListNode.create([]), ListNode.create([])))
ListNode.output(s.mergeTwoLists(ListNode.create([1, 2]), ListNode.create([])))
ListNode.output(s.mergeTwoLists(ListNode.create([1,2,3,4,5]), ListNode.create([6,7,8,9])))
ListNode.output(s.mergeTwoLists(ListNode.create([1,3,5]), ListNode.create([2,3,4,6])))
# ListNode.output(s.mergeTwoLists(ListNode.create([1, 2]), 2))
# ListNode.output(s.mergeTwoLists(ListNode.create([1, 2, 3]), 4))