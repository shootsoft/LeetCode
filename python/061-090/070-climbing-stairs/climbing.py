class Solution:
    # @param n, an integer
    # @return an integer

    def climbStairs(self, n):

        if n <= 2:
            return n
        else:
            step = [0 for i in range(n)]

            step[0] = 1
            step[1] = 2

            for i in range(2,n,1):
                step[i] = step[i-1] + step[i-2]

            return step[n-1]


    def climbStairs2(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n >=3:
            return self.climbStairs(n-1) + self.climbStairs(n-2)


s = Solution()
print s.climbStairs(3)
print s.climbStairs(4)
print s.climbStairs(5)
print s.climbStairs(6)
print s.climbStairs(7)
print s.climbStairs2(8)
print s.climbStairs(8)
