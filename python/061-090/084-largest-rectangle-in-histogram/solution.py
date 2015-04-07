__author__ = 'yinjun'

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):

        l = len(height)
        #sq = [[0 for col in range(l)] for row in range(l)]
        max = 0

        for i in range(l - 1):
            min = height[i]
            for j in range(i + 1, l):
                if height[j] < min:
                    min = height[j]
                s = min * (j - i + 1)
                #print i, j, s
                if s > max:
                    max = s

        return max

