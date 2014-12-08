class Solution:
    # @return an integer
    def reverse(self, x):
        # symbol
        s = 1
        if(x<0) :
        	s = -1
        	x *= -1
        l = list(str(x))
        l.reverse()
        x =  int(''.join(l))
        #shit
        if(x>2147483647):
        	return 0
        elif x<-2147483648:
        	return 0
        else:
        	return s * x;

s = Solution()
print s.reverse(1534236469)
print s.reverse(-123)
