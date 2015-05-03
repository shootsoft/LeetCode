class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        return list(set(self.gen('', n)))

    def gen(self, root, n):
        if n == 0:
            return ['']
        elif n == 1:
            return ['()']
        else:
            root = self.gen(root, n-1)

            #['()()','(())']
            l = n * 2
            rs =[]
            c = len(root)
            for j in range(c):
                 for i in range(l/2+1):
                    rs.append(self.plus(root[j], i))
            return rs

    def plus(self, str, pos):
        if pos == 0:
            return str+'()'
        else :
            return str[0:pos]+'()'+str[pos:]

s = Solution()
print s.generateParenthesis(0)
print s.generateParenthesis(1)
print s.generateParenthesis(2)
print s.generateParenthesis(3)
print s.generateParenthesis(4)
print s.generateParenthesis(5)
print s.generateParenthesis(6)