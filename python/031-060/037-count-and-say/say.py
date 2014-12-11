class Solution:
    # @return a string
    def countAndSay(self, n):

        if n<1:
            return ''
        i = 1
        num = '1'
        while i<n:

            num = self.say(num)

            i += 1

        return num

    def say(self, num):

        r = []
        c = len(num)
        start = 0
        if c == 1:
            r.append('1')
            r.append(num[0])
            start += 1

        while start < c:

            end = start + 1
            while end< c and num[end] == num[start]:
                end+=1

            r.append(str(end - start))
            r.append(num[start])
            start = end

        return ''.join(r)


s = Solution()
print s.countAndSay(0)
print s.countAndSay(1)
print s.countAndSay(2)
print s.countAndSay(3)
print s.countAndSay(4)
print s.countAndSay(5)
print s.countAndSay(6)