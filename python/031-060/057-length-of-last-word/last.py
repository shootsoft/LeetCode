class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        l = len(s)
        if (l==0) :
            return 0
        pos = l - 1

        c = 0
        while pos >= 0:

            if c > 0 and s[pos] == ' ':
                break
            elif s[pos] != ' ':
                c += 1

            pos -= 1

        return c

s = Solution()
print s.lengthOfLastWord('Hello world')
print s.lengthOfLastWord('Hello world ')
print s.lengthOfLastWord(' ')
print s.lengthOfLastWord(' world ')
print s.lengthOfLastWord('world')
print s.lengthOfLastWord('')