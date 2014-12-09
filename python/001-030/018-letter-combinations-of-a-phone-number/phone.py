class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        m = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
             '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
             '8':['t','u','v'], '9':['w','x','y','z'], '0':[], '1':[]}

        s = digits
        l = len(s)
        if l == 0:
            return ['']
        elif l == 1:
            return m[s[0]]

        r = m[s[0]]
        i = 1
        while(i<l):
            r = self.mutiple(r, m[s[i]])
            i += 1
        return r

    def mutiple(self, left, right):

        rs = []
        l = len(left)
        r = len(right)

        if l == 0:
            return right
        elif r == 0:
            return left

        for i in range(l):
            for j in range(r):
                rs.append( left[i]+right[j] )
        return rs

s = Solution()

print s.letterCombinations('23')