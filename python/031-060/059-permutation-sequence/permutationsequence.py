class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def getPermutation(self, n, k):


        num = [str(i) for i in range(1, n+1)]
        self.A = []
        self.max = k
        self.count = 0
        self.permuteN(num, 0, len(num)-1)

        return  self.A

    def permuteN(self, num, k, m):

        if k == m:
            self.A.append(''.join(num))
            self.count += 1
            if self.count == self.max:
                    return
        else:
            for i in range(k, m+1):

                self.swap(num, k, i)
                self.permuteN(num, k+1, m)
                if self.count == self.max:
                    return
                self.swap(num, k, i)

    def swap(self, num, k, i):
        t = num[k]
        num[k] = num[i]
        num[i] = t


s = Solution()
print s.getPermutation(5, 10)