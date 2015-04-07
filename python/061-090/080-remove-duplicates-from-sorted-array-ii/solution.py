__author__ = 'yinjun'

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        count = 0
        B =[]
        offset = 0
        last = None
        lastCount = 0
        for i in range(len(A)):
            n = A[i]
            if last == None or  n != last:
                last = n
                lastCount = 1
                #B.append(n)
                count += 1
            elif n == last and lastCount == 1:
                last = n
                lastCount = 2
                count += 1
                #B.append(n)
            else:
                B.append(i - offset)
                offset += 1
        #print offset, B

        while offset > 0 :
            del A[B[0]]
            del B[0]
            offset -= 1

        #A = B
        #print A
        return count