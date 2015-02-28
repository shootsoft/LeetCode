__author__ = 'yinjun'

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):

        # p0 = 0
        # p1 = self.count(A, 0)
        # p2 = p1 + self.count(A, 1)

        p0 = self.count(A, 0)
        p = [0,  p0, p0 + self.count(A, 1)]
        l = len(A)

        for i in range(3):
            for j in range(l):
                #print i,j
                if A[j] == i:

                    if p[i] != j:
                        p[i] = self.getNextPos(A, l, i, p[i])
                        #print 'next pos', p[i]
                        if p[i]<l:
                            self.switch(A, j, p[i])
                    p[i] += 1


        return

    def count(self, A, target):
        total = 0
        for i in A:
            if i == target:
                total +=1
        return total

    def getNextPos(self, A, length, val, start):
        r = start
        for i in range(start, length):
            if A[i] != val:
                r = i
                break
        return r



    def switch(self, A, i, j):
        #print i, j
        x = A[i]
        A[i] = A[j]
        A[j] = x