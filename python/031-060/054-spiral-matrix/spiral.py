class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):

        r =[]
        n = len(matrix)
        m = 0
        if n>0:
            m = len(matrix[0])

        i = 0
        j = 0

        count = m*n
        maxn = n
        minin = 0
        maxm = m
        minim =-1

        l = 0

        d = 0

        while l<count:
            r.append(matrix[i][j])
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
print s.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])



