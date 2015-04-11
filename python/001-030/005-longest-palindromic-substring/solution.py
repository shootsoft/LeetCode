class Solution:
    # @return a string
    def longestPalindrome(self, s):
        l = len(s)
        if s == None or l == 0:
            return ''
        maxLen = 0
        result = ''

        for i in range(l*2-1):
            left = i/2
            right = i/2
            if i%2 == 1:
                right +=1
            s2 = self.lengthOfPalindrome(s, l, left, right)
            sl = len(s2)
            if maxLen < sl:
                maxLen = sl
                result = s2
        return result

    def lengthOfPalindrome(self, s, l, left, right):
        #print s, l, left, right
        while left >=0 and right<l and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]