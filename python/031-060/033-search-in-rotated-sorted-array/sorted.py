class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):

        if A == None or A ==[]:
            return -1

        l = len(A)
        r = -1

        #shit...
        for i in range(l):
            if A[i] == target:
                r = i

        return r



s = Solution()
print s.search([], 0)

