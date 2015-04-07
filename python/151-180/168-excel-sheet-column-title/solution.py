class Solution:
    # @return a string
    def convertToTitle(self, num):

        result = []

        while num > 26:
            c = num % 26
            if c == 0:
                result.append('Z')
            else:
                result.append(str(unichr(64 + c)))
            num = (num-1) / 26


        result.append(str(unichr(64 + num)))

        result.reverse()
        return ''.join(result)

