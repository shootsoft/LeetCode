class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):

        l = len(A)
        r = l
        
        b = {}
        
        for i in range(1, l):
            if A[i] == A[i-1]:
                b[i] = 1
                r -= 1
        B = []
        for i in range(l):
            if i not in b:
                B.append(A[i])
        A = B
        print A
        return r


s = Solution()
print s.removeDuplicates([1,1,2])