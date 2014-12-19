class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):

        result = []

        length = len(words)
        i = 0
        c = 0
        sublength =0
        sub = []
        while i < length:
            lc = len(words[i])
            #print 'lc=',lc
            c += lc + 1
            sublength += lc

            #print lc, c, sublength

            if c < L:
                sub.append(words[i])
            elif c==L or c-1==L:
                sub.append(words[i])
                #print sub
                result.append(self.joinWords(sub, L, sublength, i == length-1))
                sub = []
                c = 0
                sublength = 0
            elif c>L:
                result.append(self.joinWords(sub, L, sublength-lc, False))
                sub = [words[i]]
                c = lc+1
                sublength = lc
            i += 1

        if c>0:
            print sub
            result.append(self.joinWords(sub, L, sublength, True))
        return result

    def joinWords(self, words, L, sublength, isLast):
        count = len(words)

        if count ==1 :
            #print sublength
            return words[0] + (' ' * (L-sublength))
        else:
            avg = (L - sublength) / (count -1)
            right = (L - sublength) % (count -1)
            avgs = ' ' * avg
            rights = ''

            if isLast:
                avgs = ' '
                rights = (L - sublength - count+1) * ' '


            result = words[0] + avgs


            if isLast == False and right>0:
                result += ' '
                right -= 1

            for i in range(1, count-1):
                result += words[i] + avgs
                if isLast == False and right>0:
                    result += ' '
                    right -= 1
                #print result

            result += words[count-1]

            if isLast == True:
                result += rights


            return  result

s = Solution()

print s.fullJustify([""], 2)
print s.fullJustify(["0"], 2)
print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print s.fullJustify(["What","must","be","shall","be."], 12)
print s.fullJustify(["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."], 30)
print s.fullJustify(["My","momma","always","said,","\"Life","was","like","a","box","of","chocolates.","You","never","know","what","you're","gonna","get."], 20)

