class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if(p == s):
        	return True
        elif(p == ''):
        	return False

        l = len(p)
        c = p[l-1]
        if(c!='.' and c!='*'):
        	return self.isMatchDirection(s, p, 1)
        else :
        	return self.isMatchDirection(s, p, 0)
        '''
        print 'p1=', p1
        if(p1):
        	return p1
        else:
        	p2 = self.isMatchDirection(s, p, 1)
        	print 'p2=', p2
        	return p2
        '''

    def isMatchDirection(self, s, p, d):
    	ls = list(s)
        lp = list(p)
        leftpop = True
        rightpop = True
        left = None
        right = None
        
        while(len(ls)>0 and len(lp)>0):

        	if leftpop == True:
        		if(d==0):
        			left = ls[0]
        			ls.remove(left)
        		else:
        			left = ls.pop()
        	if rightpop == True:
        		if(d==0):
        			right = lp[0]
        			lp.remove(right)
        		else:
        			right = lp.pop()

        	if(right == '.' or (left == right and right != '*')):
        		leftpop = True
        		rightpop = True
        		
        	elif(right == '*'):
        		leftpop = True
        		rightpop = False
        		#print ls, lp
        	else :
        		leftpop = True
        		rightpop = False

       	#print d, ls, lp, right 

        if len(ls) >0 and len(lp) ==0 :
        	return False 
        elif len(ls)==0 and right == '*':
        	return True
        elif(len(ls)==0 and len(lp)==0):
        	return True
        else:
        	return False


s = Solution()

print s.isMatch("aaa", "ab*a"), False
print s.isMatch("aab", "c*a*b"), True # true
print s.isMatch("aaa", "a.a"), True
print s.isMatch("ab", ".*c"), False #false
print s.isMatch("aa","aa"), True # true
print s.isMatch("abcd", "d*"), False # false
print s.isMatch("aa","a") , False# false
print s.isMatch("aaa","aa"), False # false
print s.isMatch("aa", "a*"), True # true
print s.isMatch("aa", ".*"), True # true
print s.isMatch("ab", ".*"), True # true