class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):

        self.A = {}
        self.permuteN(num, 0, len(num)-1)

        return  self.A.values()

    def permuteN(self, num, k, m):

        if k == m:
            self.A[''.join(map(str, num))]= num[:]
        else:

            for i in range(k, m+1):

                if i>0 and num[m] == num[k+1]:
                    continue
                    #self.permuteN(num, k+1, m)
                #else:
                self.swap(num, k, i)
                self.permuteN(num, k+1, m)
                self.swap(num, k, i)

    def swap(self, num, k, i):
        t = num[k]
        num[k] = num[i]
        num[i] = t


s = Solution()
print s.permuteUnique([3,3,1,2,3,2,3,1])