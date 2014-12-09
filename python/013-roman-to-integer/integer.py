class Solution:
    # @return an integer
    def romanToInt(self, s):
        v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        k = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", "M"]
        r = 0
        #l = list(s).reverse()

        while s!='' and len(v)>0 and len(k)>0 :
            num = v.pop()
            key = k.pop()
            while s.startswith(key):
                r += num
                s = s[len(key):]

        return r


s = Solution()
print s.romanToInt('XXX')
print s.romanToInt('MMMXCIX')
print s.romanToInt('MMMCMXCIX')
print s.romanToInt('CMXCIX')
print s.romanToInt('MMMIX')
print s.romanToInt('XCIX')
print s.romanToInt('XIX')
print s.romanToInt('IX')
print s.romanToInt('M')
print s.romanToInt('I')