class Solution:
    # @return a string
    def longestPalindrome(self, s):
        max_sub = ''
        max_len = 0
        str_len = len(s)

        if s is '' or str_len==1:
        	return s

        pos = str_len / 2

        while pos > 0:
        	sub = self.longestPalindrome1(s, pos, str_len)
        	sub_len = len(sub)
        	if sub_len > max_len:
        		max_sub = sub
        		max_len = sub_len

        	sub = self.longestPalindrome2(s, pos, str_len)
        	sub_len = len(sub)
        	if sub_len > max_len:
        		max_sub = sub
        		max_len = sub_len

        	pos -= 1

        while pos < str_len:
        	sub = self.longestPalindrome1(s, pos, str_len)
        	sub_len = len(sub)
        	if sub_len > max_len:
        		max_sub = sub
        		max_len = sub_len

        	sub = self.longestPalindrome2(s, pos, str_len)
        	sub_len = len(sub)
        	if sub_len > max_len:
        		max_sub = sub
        		max_len = sub_len

        	pos += 1

        return max_sub

    #type 1 abcba
    def longestPalindrome1(self, s, pos, l):

    	start = pos - 1
    	end = pos + 1
    	last_start = pos
    	last_end = pos
    	while start >=0 and end < l and s[start] is s[end]:
    		last_start = start
    		last_end = end
    		start -=1
    		end +=1

    	return s[last_start:last_end+1]

    #type 2 abba abbac
    def longestPalindrome2(self, s, pos, l):

    	start = pos - 1
    	end = pos
    	last_start = pos
    	last_end = pos
    	while start >=0 and end < l and s[start] is s[end]:
    		last_start = start
    		last_end = end
    		start -=1
    		end +=1

    	return s[last_start:last_end+1]



s = Solution()
print s.longestPalindrome('')
print s.longestPalindrome('a')
print s.longestPalindrome('abxba')
print s.longestPalindrome('abba')
print s.longestPalindrome('aba')
print s.longestPalindrome('xabay')
print s.longestPalindrome('xabbay')
print s.longestPalindrome('xabcbay')
print s.longestPalindrome('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')