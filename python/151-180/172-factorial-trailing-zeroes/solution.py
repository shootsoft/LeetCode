class Solution:
    # @return an integer
    def trailingZeroes(self, n):

        r = 0

        while n>=5:

            c = n/5
            r += c
            n = c

        return r