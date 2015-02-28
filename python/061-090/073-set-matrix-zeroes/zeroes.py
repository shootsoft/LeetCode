class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):

        iz = list()
        jz = list()
        n = len(matrix)
        m = 0
        if n>0:
            m = len(matrix[0])
        else:
            return

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0 :
                    iz.append(i)
                    jz.append(j)


        while len(iz)>0:
            i = iz.pop()
            for j in range(m):
                matrix[i][j] = 0

        while len(jz)>0 :
            j = jz.pop()
            for i in range(n):
                matrix[i][j] = 0


        return

s = Solution()
m = [[0,1]]
s.setZeroes(m)
print m