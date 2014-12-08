class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if(x<0):
        	return False
        s = str(x)
        l = len(s)
        start = 0
        end = l -1
        while(start < end and s[start] == s[end]):
        	start +=1
        	end -=1
        	if(start==end or start>end):
        		return True
        
        return False

s = Solution()
print s.isPalindrome(121)
print s.isPalindrome(1121)
print s.isPalindrome(11)
print s.isPalindrome(11111)
print s.isPalindrome(-11121)
print s.isPalindrome(-2147447412)