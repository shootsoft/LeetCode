__author__ = 'yinjun'

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