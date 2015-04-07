__author__ = 'yinjun'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):

        if m == n:
            return head

        h = ListNode(0)
        h.next = head
        hm = h
        hn = h.next

        i = 1
        while i < m:
            i += 1
            hm = hm.next
            hn = hn.next
            print "hm ", hm.val


        while i < n:

            print i, h.next.toList(), 'hn.val=', hn.val

            p = hn.next
            tail = p.next

            p.next = hm.next
            hm.next = p
            hn.next = tail
            i += 1

        return h.next



class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def toList(self):

        v = [self.val]
        c = self.next
        while c!=None:
            v.append(c.val)
            c = c.next
        return v

    @staticmethod
    def fromList(list):
        head = ListNode(0)
        h = head
        for v in list:
            n = ListNode(v)
            h.next = n
            h = h.next

        return head.next


    @staticmethod
    def createLists(lists):
        l = []
        c = len(lists)
        for i in range(c):
            li = list(lists[i])
            lic = len(li)
            head = ListNode(0)
            chead = head
            #print lists[i]
            for j in range(lic):
                chead.next = ListNode(li[j])
                chead = chead.next
            l.append(head.next)



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
head = ListNode.fromList([1,2,3,4])
print 'head', head.toList()
result = s.reverseBetween(head, 1, 4)
print result.toList()