class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
    	length = len(s)
    	m = 0     #max
    	cur = 0   #cur length
    	i = 1	  #index
    	if length > 0 :
	    	d = {s[0]:0}
	    	start = 0 # start index
	    	m = 1 # update min length
	    	cur = 1 # update min value
	    	while(i<length):
	    		if s[i] in d :
	    			end = d[s[i]]
	    			#remove old duplicate character
	    			while(start<=end):
	    				del d[s[start]]
	    				start = start+1
	    			start = end + 1
	    			d[s[i]] = i
	    			cur = len(d)
	    		else:
	    			d[s[i]] = i
	    			cur =cur + 1
	    			if cur > m:
	    				m = cur
	    		i = i+1
        return m
    

s = Solution()
print s.lengthOfLongestSubstring('abcbdabbbcc')
print s.lengthOfLongestSubstring('bbbb')
print s.lengthOfLongestSubstring('')
print s.lengthOfLongestSubstring('a')
print s.lengthOfLongestSubstring('ruowzgiooobpple')


