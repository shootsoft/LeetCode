class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, num1, num2):
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
            if x >= 2 :
                x -= 2
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

            if x >= 2 :
                x -= 2
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

            if x >= 2 :
                x -= 2
                add = 1

            result[pos] = chr(x+48)
            pos += 1
            pos2 -= 1
        if add > 0:
            result[pos] =chr(add+48)
        result.reverse()
        return ''.join(result)


s = Solution()
print s.addBinary('1111','1')
print s.addBinary('1111','1010')
