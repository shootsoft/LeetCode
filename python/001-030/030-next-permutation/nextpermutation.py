__author__ = 'yinjun'

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, target):

        self.target = target
        self.find = False
        self.result = []

        length = len(target)
        if length <= 1:
            return target
        else:
            num = range(1, length + 1)
            self.permuteN(num, 0, len(num)-1)

        return self.result

    def permuteN(self, num, k, m):

        if k == m:

            if self.target == num:
                self.find = True
            elif self.find and self.result == []:
                self.result = num[:]
                return
        else:
            for i in range(k, m+1):

                self.swap(num, k, i)
                self.permuteN(num, k+1, m)
                if self.find and self.result != []:
                    return
                self.swap(num, k, i)


    def swap(self, num, k, i):
        t = num[k]
        num[k] = num[i]
        num[i] = t

s = Solution()
print s.nextPermutation([])
print s.nextPermutation([1])
print s.nextPermutation([1,2,3])
print s.nextPermutation([1,3,2])



