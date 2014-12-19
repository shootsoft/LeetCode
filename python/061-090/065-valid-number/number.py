class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):

        length = len(s)
        start = -1
        end = -1
        dot = False
        e = False
        if length ==0 :
            return False
        #  ascii whitespace = 32  + = 43 - = 45 dot = 46 0 = 48 9 = 57  e = 101

        start = -1
        for i in range(length):
            if s[i]!=' ':
                start = i
                break

        if start==-1:
            return False

        end = - 1
        for i in range(length-1, -1, -1):
            n = ord(s[i])
            if s[i]!=' ':
                end = i + 1
                break
        s = s[start:end]

        length = len(s)
        if length ==0 :
            return False

        symbol = {}
        number = None
        dot = False
        e = False
        for i in range(length):
            n = ord(s[i])

            if n==43 and i == 0 and i < length-1:
                continue

            elif n == 45 and i == 0 and i < length-1:
                v = -1
                continue
            elif n == 46 and dot==False and e == False:
                dot = True
                if number==None and i < length-1:
                    n = ord(s[i+1])
                    if n>=48 and n<=57:
                        number = 0
                        continue
                    else:
                        return False
            elif n == 101 and e == False and number !=None and i< length-1:
                e = True
                return self.isInteger(s, length, i+1)

            elif n>=48 and n<=57: # 0~9
                if number == None:
                    number = 1
            else:
                return False

        if number == None:
            return False

        return True

    def isInteger(self, s, length, start):

        if s[start] == '+' or s[start]=='-':
            start +=1
        if length-start<1:
            return False
        result = True
        for i in range(start, length):
            n = ord(s[i])
            if n<48 or n>57:
                result = False
                break
        #print s, length, start, result
        return result


s = Solution()
print s.isNumber("2e0"), True
print s.isNumber("6e6.5"), False
print s.isNumber(".e1"), False
print s.isNumber(".1"), True
print s.isNumber("."), False
print s.isNumber("-"), False
print s.isNumber(" - "), False

print s.isNumber("-1"), True
print s.isNumber("-0"), True
print s.isNumber("0"), True
print s.isNumber(" 0.1 " ), True
print s.isNumber(" -0.1 " ), True
print s.isNumber("abc" ), False
print s.isNumber("1 a" ), False
print s.isNumber("2e10" ), True