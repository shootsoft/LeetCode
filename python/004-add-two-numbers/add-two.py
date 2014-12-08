# Definition for singly-linked list.
# class ListNode:
# def __init__(self, x):
# self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        r = ListNode(0)
        cur = r

        while True:

            val1 = 0
            val2 = 0
            if l1 is not None:
                val1 = l1.val

            if l2 is not None:
                val2 = l2.val

            #print 'before ', cur.val
            cur.val = cur.val + val1 + val2
            #print 'after ',cur.val

            if cur.val >= 10:
                cur.val -= 10
                cur.next = ListNode(0)
                cur.next.val = 1

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

            if l1 is not None or l2 is not None:

                if cur.next is None:
                    cur.next = ListNode(0)

                cur = cur.next


            if l1 is None and l2 is None:
                break

        return r


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def create(numbers):
        head = ListNode(numbers[0])
        next = head
        i = 1
        l = len(numbers)
        while i<l:
            next.next = ListNode(numbers[i])
            next = next.next
            i += 1
        return head

    @staticmethod
    def output(n):
        b = n
        print '['
        while b != None:
            print b.val
            b = b.next
        print ']'

#a = ListNode(0)
#b = ListNode(0)
#s = Solution()
#r = s.addTwoNumbers(a, b)
#while r!=None:
#	print r.val
#	r = r.next

'''
a = ListNode(9)
a.next = ListNode(8)
a.next.next = ListNode(7)
b = ListNode(0)
s = Solution()
r = s.addTwoNumbers(a, b)
print 'return'
while r != None:
    print r.val
    r = r.next
'''

a = ListNode.create([7,0,3,6,7,3,2,1,5])
b = ListNode.create([9,2,5,5,6,1,2,2,4])

ListNode.output(a);
ListNode.output(b);

s = Solution()
r = s.addTwoNumbers(a, b)
print 'return'
ListNode.output(r);


#{}, {}
