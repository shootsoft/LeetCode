class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):

        l = len(A)
        r = 0

        find = False
        for i in range(l):

            if target<=A[i]:
                r = i
                find = True
                break
        if find == False:
            r = l

        return r


s = Solution()
print s.searchInsert([1], 2)