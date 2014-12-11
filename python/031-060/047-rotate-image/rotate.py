class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):

        n = len(matrix)
        m = 0

        if n>0:
            m = len(matrix[0])
        else:
            return matrix

        r = [0] * m
        for i in range(m):
            r[i] = [0] * n

        for i in range(n):
            for j in range(m):
                r[j][n-1-i] = matrix[i][j]

        return r


s = Solution()
print s.rotate([
    [0,1,2,3],
    [4,5,6,7]

])