class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):

        length = len(A)

        if length < 2:
            return 0


        count = 0
        start = -1
        pos = 0
        while pos<length:

            if A[pos] > 0 :
                start = pos
                end = self.findNextHigh(A, length, start)

                if end - start <= 1:
                    pos += 1
                    continue

                count += self.count(A, start, end)
                pos = end
            else:
                pos += 1

        return count

    def findNextHigh(self, A, length, start):

        if length - start == 1:
            return -1

        max = -1
        for i in range(start + 1, length):
            if max == -1 or A[i] >= A[max]:
                max = i
                if A[max] >= A[start]:
                    break
        return max

    def count(self, A, start, end):
        if end - start < 2:
            return 0

        count = 0
        height = A[start]
        if A[end] < height:
            height = A[end]

        #print start, end, height

        for i in range(start + 1, end ):
            #print  height, A[i]
            if height - A[i] > 0:
                count += height - A[i]

        return count


s = Solution()
print s.trap([5,2,1,2,1,5])
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print s.trap([4,2,3])