class Solution:    
	# @return a string
    def intToRoman(self, num):
        l ={'1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI',
        '7':'VII','8':'VIII','9':'IX','10':'X','11':'XI','12':'XII',
        '13':'XIII','14':'XIV','15':'XV','16':'XVI','17':'XVII',
        '18':'XVIII','19':'XIX','20':'XX','30':'XXX','40':'XL',
        '50':'L','60':'LX','70':'LXX','80':'LXXX','90':'XC','100':'C',
        '200':'CC','300':'CCC','400':'CD','500':'D','600':'DC','700':'DCC',
        '800':'DCCC','900':'CM','1000':'M'}
        r = ''
        s = list(str(num))
        if num>=1000 :
        	t = int(s[0])
        	s.remove(s[0])
        	r += l['1000'] * t
        	num -= 1000 * t




        if num >=100:
            t = int(s[0])
            s.remove(s[0])

            if t>0:
        	    r+= l[str(100 * t)]
        	    num -= 100 * t
        elif r!='':
            t = int(s[0])
            s.remove(s[0])

        if num > 20:
            t = int(s[0])
            s.remove(s[0])
            r += l[str(10 * t)]
            num -= 10 * t

        if num>0:
        	r += l[str(num)]

        return r


s = Solution()

print s.intToRoman(30)
print s.intToRoman(3099)
print s.intToRoman(3999)
print s.intToRoman(999)
print s.intToRoman(3009)
print s.intToRoman(99)
print s.intToRoman(19)
print s.intToRoman(9)
print s.intToRoman(1000)
print s.intToRoman(1)