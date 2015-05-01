class Solution:


    # @return a boolean
    def isMatch(self, s, p):

        if(p == s):
        	return True
        elif(p == ''):
        	return False

        lens = len(s)
        lenp = len(p)

        left = 0
        right = 0

        return self.isMatchSub(s, p, lens, lenp, left, right)


    def isMatchSub(self, s, p, lens, lenp, left, right):

        if left == lens and right ==lenp:
            return True

        if right + 1 < lenp and p[right+1] == '*':

            while left < lens and ( p[right] == '.' or s[left] == p[right] ):

                if self.isMatchSub(s, p, lens, lenp, left, right + 2):
                    return True
                left += 1

            return self.isMatchSub(s, p, lens, lenp, left, right + 2)

        elif left < lens and right < lenp and (p[right] == '.' or s[left] == p[right]):

            return self.isMatchSub(s,p, lens, lenp, left + 1, right + 1)


        return False