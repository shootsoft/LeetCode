__author__ = 'yinjun'

class Solution:
    # @return a string
    def minWindow(self, S, T):
        c = self.countTZan(T)
        end = c -1
        start = 0
        minlen = -1
        minstr = ""
        for end in range(end, len(S)):
            sub = S[start:end]
            zan = self.countZan(sub)

            while(zan == c):
                l = len(sub)
                if minlen == -1 or minlen < l:
                    minstr = sub[:]
                    minlen = l

                start+=1

                if start == end:
                    break
                sub = S[start:end]
                zan = self.countZan(sub)

        return minstr

    def countTZan(self, T):
        self.zan = {}
        for i in T:
            self.zan[i] = 1
        return len(self.zan)

    def countZan(self, sub):
        sz = {}

        for i in sub:
            if i in self.zan:
                sz[i] = 1

        return len(sz)