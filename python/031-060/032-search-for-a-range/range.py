class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):

        l = len(A)
        s = -1
        e = -1

        for i in range(l):

            if A[i]>target:
                if s >-1:
                    e = i-1
                break
            elif A[i] < target:
                continue
            else:
                if s == -1:
                    s = i
                e = i

        if s>-1 and e == -1:
            e = 0

        return [s, e]

s = Solution()
print s.searchRange([5, 7, 7, 8, 8, 10], 8)