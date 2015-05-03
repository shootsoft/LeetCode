class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):

        A.sort()
        l = len(A)
        i = 0
        c = 0
        while i<l:
            if A[i] != elem:
                A[c] = A[i]
                c +=1
            i += 1
        return c