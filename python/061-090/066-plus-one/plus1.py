class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):

        result=[]
        length = len(digits)
        if length ==0:
            return result

        plus = 0
        p = False

        n = digits.pop()
        length -= 1
        n += 1
        if n>= 10:
            plus = 1
            n -= 10
        result.append(n)
        while(length>0):
            n = digits.pop()
            if plus>0:
                n += plus
                plus = 0
            if n>= 10:
                plus = 1
                n -= 10
            length -= 1
            result.append(n)

        if plus > 0:
            result.append(1)

        result.reverse()

        return result

s = Solution()
print s.plusOne([1,2])
print s.plusOne([9,9])