class Solution:
    # @param n,
    # @return a matrix
    def generateMatrix(self, n):

        r =[0] * n
        for i in range(n):
            r[i] = [0] * n
        m = n

        i = 0
        j = 0

        count = n*n
        maxn = n
        minin = 0
        maxm = m
        minim =-1

        l = 1

        d = 0

        while l<=count:
            r[i][j]= l
            l += 1
            if d == 0:
                j += 1
                if j== maxm:
                    maxm -= 1
                    j -= 1
                    i += 1
                    d = 1
            elif d == 1:
                i += 1
                if i== maxn:
                    maxn -= 1
                    i -= 1
                    j -= 1
                    d = 2
            elif d == 2:
                j -= 1
                if j== minim:
                    minim += 1
                    j += 1
                    i -= 1
                    d = 3
            else:
                i -= 1
                if i == minin:
                    minin += 1
                    i += 1
                    j += 1
                    d = 0
        return r


s = Solution()
print s.generateMatrix(3)
print s.generateMatrix(4)



