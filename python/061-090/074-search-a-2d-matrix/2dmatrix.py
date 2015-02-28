class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):

        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])

        i = -1

        r = False

        for x in range(n):
            if matrix[x][0]==target:
                return True
            elif matrix[x][0] < target:
                i = x
            else:
                break

        if i == -1 :
            return False

        for x in range(m):
            if matrix[i][x] == target:
                return True
            elif matrix[i][x] < target:
                continue
            else:
                break

        return False




s = Solution()
print s.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3)