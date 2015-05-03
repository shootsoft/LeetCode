class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        r = []
        toFind = {}
        find = {}

        length = len(L)
        step = len(L[0])

        for i in xrange(length):
            s = L[i]
            if s in toFind:
                toFind[s] += 1
            else:
                toFind[s] = 1

        for i in xrange(len(S) - length * step):
            find = {}
            j = 0
            #isBreak = False
            for j in xrange(length + 1):
                if j == length:
                    r.append(i)
                    break
                s = i + j * step
                word = S[s:s+step]

                if word in toFind:

                    if word in find:
                        find[word] += 1
                    else:
                        find[word] = 1

                    if find[word]> toFind[word]:
                        isBreak = True
                        #break


                else:
                    #isBreak = True
                    break

        return r