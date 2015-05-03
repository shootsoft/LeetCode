class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        lt = len(s)

        if s==None or lt ==0:
            return 0

        t = list(s)
        h = [t.pop(0)]
        lh = 1
        lt -= 1

        longest = 0  #longest length
        cur = 0      #length
        p = 1

        while lh > 0 and lt > 0:


            left = h.pop()
            right = t.pop(0)
            if left == '(' and right ==')':
                lt -= 1
                lh -= 1
                p -= 1

                cur += 2
                if cur > longest:
                    longest = cur

            elif lt >0:

                print '*', cur, p, lh, lt

                h.append(left)
                h.append(right)
                lt -=1
                lh += 1
                p += 1

                 #reset
                if right == ')':
                    cur = 0





            if lh == 0 and lt > 0:
                lh += 1
                lt -= 1
                right = t.pop(0)
                h.append(right)
                p += 1
                #reset
                if right == ')':
                    cur = 0
            #if p > 1 and lh > lt:
            #    cur =0


        return longest


s = Solution()
print 4, s.longestValidParentheses("(()()")
print 2, s.longestValidParentheses("()(()")
print s.longestValidParentheses("()()")
print s.longestValidParentheses("()()()")
print s.longestValidParentheses("(()())")
print s.longestValidParentheses("((()))")
print s.longestValidParentheses(")((()))")

