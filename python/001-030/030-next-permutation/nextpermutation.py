__author__ = 'yinjun'

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):

        l = len(num)
        for i in range(1, l):
            if num[i] > num[i+1]:
                x = num[i-1]
                num[i-1] = num[i]
                num[i] = x

        return num


s = Solution()
print s.nextPermutation([1,2,3])
print s.nextPermutation([1,3,2])



