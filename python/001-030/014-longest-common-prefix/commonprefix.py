class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        r = ''
        l = len(strs)
        i = 0

        if l==0:
            return r
        elif l==1 :
            return strs[0]

        ls = [1]*l
        for x in range(l):
            ls[x] = len(strs[x])


        while True:

            if i >= ls[0]:
                i -= 1
                same = False
                break

            c = strs[0][i]
            same = True

            for j in range(1, l):

                if i>=ls[j] or strs[j][i] != c:
                    i -=1
                    same = False
                    break

            if same == False :
                break
            else :
                i +=1

        if i>=0:
            r = strs[0][0:i+1]

        return r



s = Solution()

print s.longestCommonPrefix(["", "", ""])
print s.longestCommonPrefix([])
print s.longestCommonPrefix([""])
print s.longestCommonPrefix(["", "Abc", ""])
print s.longestCommonPrefix(["Abe", "Abd", "Abc"])
print s.longestCommonPrefix(["Abe", "Abd", "Ab"])