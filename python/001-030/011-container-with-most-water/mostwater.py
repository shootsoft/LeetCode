class Solution:
    # @return an integer
    def maxArea(self, A):

        length = len(A)
        if length < 2:
            return 0


        max = 0
        pos = 0
        while pos<length:

            area =

        return max

    def findNextHigh(self, A, length, start):

        max = start
        for i in range(start + 1, length):
            if max == -1 or A[i] >= A[max]:
                max = i
                if A[max] >= A[start]:
                    break
        return max

    def count(self, A, start, end):

        if end == start:
            return end * A[start]

        height = A[start]
        if A[end] < height:
            height = A[end]

        return height * (end - start)

        #print start, end, height

        #for i in range(start + 1, end ):
        #    #print  height, A[i]
        #    if height - A[i] > 0:
        #        count += height - A[i]

        return count


s = Solution()
print s.maxArea([1,1])
print s.maxArea([4,6,2,6,7,11,2])