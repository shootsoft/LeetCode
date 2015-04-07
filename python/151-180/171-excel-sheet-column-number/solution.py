__author__ = 'yinjun'

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):

        lst = list(s)
        l = len(lst)
        r = l - 1
        num = 0
        pos = 0


        while pos < l:
            c = lst[pos]
            cn = ord(c) - 64
            num += cn * 26**r
            pos += 1
            r -= 1
        return num


