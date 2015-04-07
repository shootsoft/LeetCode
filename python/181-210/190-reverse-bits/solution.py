class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        lst = self.toReverseBinList(n)
        return self.toDec(lst)


    def toReverseBinList(self, n):
        r = []
        while n > 1:
            r.append( n % 2)
            n = n / 2

        r.append(n)
        l = len(r)
        if l < 32:
            r += [0] * (32-l)
        return r


    def toDec(self, lst):

        l = len(lst)
        r = l-1
        pos = 0
        n = 0

        while pos < l:


            n += lst[pos] * 2 ** r
            r -= 1
            pos += 1

        return n