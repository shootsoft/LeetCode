class Solution:
    # @return a boolean
    def isValid(self, s):
        d = {'{}': 1, '()': 1, '[]': 1}
        t = list(s)
        h = []
        lt = len(t)
        lh = 0

        if lt == 0 or lt % 2 != 0:
            return False

        while lt > 0:
            if lh == 0:
                lh += 1
                lt -= 1
                h.append(t.pop())
            else:
                hn = h.pop()
                tn = t.pop()
                if (tn + hn) in d:
                    lh -= 1
                    lt -= 1
                    continue
                else:
                        h.append(hn)
                        h.append(tn)
                        #print lt, t, h
                        lh += 1
                        lt -= 1
                #else:
                #    lt = 0

        if lt == 0 and lh == 0:
            return True
        else:
            return False


s = Solution()

print True, s.isValid('[(){()}]')
print True, s.isValid('{}')
print False, s.isValid(')(')
print True, s.isValid('[]')
print False, s.isValid("([)]")