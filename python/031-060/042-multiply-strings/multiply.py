class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):

        if num1 =='0' or num2 == '0':
            return '0'

        result = ''
        num = num1
        pos = len(num2) -1
        base = ''

        while pos >= 0:

            n = ord(num2[pos]) - 48
            num = self.mutiplyNum(num1, n)
            num += base
            result = self.plus(result, num)
            base += '0'
            pos -= 1

        return result

    def mutiplyNum(self, num, n):


        if n==0 or num == '0':
            return '0'

        m = 0
        posn = len(num) -1
        posr = posn + 2
        result = [''] * posr
        posr = 0

        while posn >=0:

            x =  ( ord(num[posn]) - 48) * n

            if m > 0:
                x += m
                m = 0

            if x >= 10 :
                s = str(x)
                x = ord(s[1]) - 48
                m = ord(s[0]) - 48
            result[posr] = chr(x+48)

            posr += 1
            posn -= 1

        if m>0:
            result[posr] = chr(m+48)

        result.reverse()
        return ''.join(result)

    def plus(self, num1, num2):

        #print num1, num2

        add = 0
        pos1 = len(num1)-1
        pos2 = len(num2)-1

        pos = pos1 + 2
        if(pos2>pos1):
            pos = pos2 + 2
        result = [''] * pos
        pos = 0
        while pos1 >=0 and pos2 >=0:
            #print pos1, pos2
            x = ord(num1[pos1]) + ord(num2[pos2]) - 96
            if add> 0:
                x += add
                add = 0
            if x >= 10 :
                x -= 10
                add = 1

            result[pos] = chr(x+48)
            pos += 1
            pos1 -= 1
            pos2 -= 1
        #print result
        while pos1 >=0:

            x = ord(num1[pos1]) - 48
            if add>0 :
                x += add
                add = 0

            if x >= 10 :
                x -= 10
                add = 1

            result[pos] = chr(x+48)
            pos += 1
            pos1 -= 1
       # print result
        while pos2 >=0:

            x =  ord(num2[pos2]) - 48
            if add>0 :
                x += 1
                add = 0

            if x >= 10 :
                x -= 10
                add = 1

            result[pos] = chr(x+48)
            pos += 1
            pos2 -= 1
        if add > 0:
            result[pos] =chr(add+48)
        result.reverse()
        return ''.join(result)

s = Solution()

print s.plus('944977892613941239847293847293847293847293847293842335269', '98762349283749283479283749283749283479283749238749238749283472938479238543120000000')


print s.multiply("123456789", "9")
print s.multiply('123', '9')
print s.multiply('123', '999')
print s.multiply('123', '0')
print s.multiply("123456789", "987654321"), 121932631112635269


print s.mutiplyNum('123', 9)
print s.mutiplyNum('123', 0)
print s.mutiplyNum('999', 9)
print s.mutiplyNum('', 9)
print s.mutiplyNum('', 0)
print s.mutiplyNum('9', 9)

print s.plus('123', '12'), 135
print s.plus('123', '123956')
print s.plus('123', '')
print s.plus('', '')
print s.plus('', '123')

