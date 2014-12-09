class Solution:
    # @return an integer
    def atoi(self, str):
        l = len(str)
        r = 0 #return
        b = 10 #base 1 10 100 1000...
        s = 1 #symbol +1 -1
       	start = False
        for i in range(l):
        	#shit...
        	c = ord(str[i])
        	#white space
        	if str[i] == ' ' and start is False:
        		continue
        	elif str[i] == '+' and start is False:
        		s = 1
        		start = True
        	elif str[i] == '-' and start is False:
        		s = -1
        		start = True
        	elif c >=48 and c<=57:
        		r = r * b + c - 48
        		start=True
        	else:
        		#exception
        		break
       	r *=s
        if r>2147483647:
        	return 2147483647
        elif r < -2147483648:
        	return -2147483648
        else:
        	return r


s = Solution()
print s.atoi('123')
print s.atoi('-123')
print s.atoi('2147483648')
print s.atoi('  -0012a42')
print s.atoi('  -2147483648')
