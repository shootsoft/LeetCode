class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        g = x
        r = g * g - x


        while r>0.000001:
            g = (g + x / g) / 2.0
            r = g * g - x
            if r < 0:
                r *= -1

        return int(g)


s = Solution();
print s.sqrt(0)
print s.sqrt(3)
print s.sqrt(4)
print s.sqrt(5)
print s.sqrt(10)
print s.sqrt(100)
print s.sqrt(99423420)