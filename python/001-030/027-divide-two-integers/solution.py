class Solution:

    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        import sys
        if divisor == 0 or dividend<-2147483648:
            return 2147483647

        dd = abs(dividend)
        dr = abs(divisor)
        result = 0
        sum = 0
        count = 0
        while dd >= dr:
            sum = dr
            count = 1

            while sum + sum <= dd:
                sum += sum
                count += count
            dd -= sum
            result += count
        if dividend>0 and divisor< 0 or dividend<0 and divisor>0:
            result = 0 - result
        
        #fuck this case
        if result > 2147483647:
            return 2147483647

        return result

