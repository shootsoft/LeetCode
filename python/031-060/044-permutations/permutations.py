class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):

        self.A = []
        self.permuteN(num, 0, len(num)-1)

        return  self.A

    def permuteN(self, num, k, m):

        if k == m:
            self.A.append(num[:])
        else:

            for i in range(k, m+1):
                self.swap(num, k, i)
                self.permuteN(num, k+1, m)
                self.swap(num, k, i)

    def swap(self, num, k, i):
        t = num[k]
        num[k] = num[i]
        num[i] = t


s = Solution()
print s.permute([1,2,3])