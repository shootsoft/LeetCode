class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):

        r = 0

        while n >= 2:
            if n % 2 == 1:
                r += 1
            n = n / 2

        if n%2 == 1:
            r += 1
        return r
