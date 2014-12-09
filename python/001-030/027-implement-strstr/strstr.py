class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):

        if needle == haystack or needle== '' :
            return 0
        elif needle== None or haystack == None or haystack=='':
            return -1

        h = len(haystack)
        n = len(needle)

        if n >= h :
            return -1

        for i in range(h-n+1):

            find = True

            for j in range(n):
                if haystack[i + j]!=needle[j]:
                    find = False
                    break

            if find:
                return i
        return -1

s = Solution()
print s.strStr("mississippi", "pi")