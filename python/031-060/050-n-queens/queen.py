class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        result =[]
        cur = set()
        mx = n*n
        i = 0
        while i< mx