# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):

        if k<=1 or head == None or head.next == None:
            return head

        pre = ListNode(0)
        pre.next = head
        rt = pre

        while(pre!=None):

            #print 'mb'
            #ListNode.output(pre)

            self.reverseK(pre, k)
            i = 0
            while i<k and pre!=None:
                pre = pre.next
                i +=1

        return rt.next



    def reverseK(self, pre, k):

        if pre==None or pre.next == None or pre.next.next == None:
            return pre

        x = pre
        i = 0
        while i<k and x!=None:
            x = x.next
            i+=1
        if i<k-1 or x == None:
            return pre

        t = pre.next
        n = t.next

        i = 1
        while i < k and n != None:

            t.next = n.next
            n.next = pre.next
            pre.next = n
            n = t.next

            #p = pre

            #while p.next != t:
            #    n = n.next
            #p = n
            #n = t.next
            #t = p

            i += 1

           # ListNode.output(pre)

        return pre







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

#ListNode.output( s.reverseK( ListNode.create([0, 1,2,3, 4]), 4 ) )

#ListNode.output( s.reverseKGroup( ListNode.create([1,2,3,4]), 4) )
ListNode.output( s.reverseKGroup( ListNode.create([1,2,3,4,5,6,7,8]), 4) )
#ListNode.output( s.reverseKGroup( ListNode.create([1,2,3,4,5]), 5) )
#ListNode.output( s.reverseKGroup( ListNode.create([1,2,3]), 3) )

#ListNode.output( s.reverseKGroup( ListNode.create([1,2,3,4, 5, 6, 7]), 2 ) )
#ListNode.output( s.reverseKGroup( ListNode.create([1,2,3,4, 5, 6, 7]), 3 ) )
#ListNode.output( s.reverseKGroup( ListNode.create([1,2]), 3 ) )

#ListNode.output( s.swapPairs( ListNode.create([1,2]) ) )