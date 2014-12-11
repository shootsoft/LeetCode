# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):

        if head == None or head.next==None or k==0:
            return head

        h = head
        i = 0
        l = 1
        t = h
        while t.next != None:
            t = t.next
            l += 1

        p = l - k
        if p ==0 :
            return head
        elif p<0:
            k = k % l
            p = l- k

        pre = None
        while i<p and h !=None:
            i += 1
            pre = h
            h = h.next

        #print  h.val, t.val

        if h == None:
            return head
        else:
            t.next = head
            if pre!=None:
                pre.next = None
            else:
                h = t
                head.next = None
            return h




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


ListNode.output(s.rotateRight(ListNode.create([1, 2, 3]), 10))
ListNode.output(s.rotateRight(ListNode.create([1, 2]), 1))
ListNode.output(s.rotateRight(ListNode.create([1,2,3,4,5]), 2))
ListNode.output(s.rotateRight(ListNode.create([1]), 1))
ListNode.output(s.rotateRight(ListNode.create([1, 2]), 2))
ListNode.output(s.rotateRight(ListNode.create([1, 2, 3]), 4))