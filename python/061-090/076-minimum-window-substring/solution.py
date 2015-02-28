__author__ = 'yinjun'

class Solution:


    # @return a string
    def minWindow(self, S, T):

        #print S, T
        lS = len(S)
        lT = len(T)
        if lT > lS:
            return ""

        c = self.countTZan(T)
        self.szan = {}

        end = c
        if end > lS:
            end = lS
        start = 0
        minlen = -1
        minstart = 0
        minend = 0



        zan = self.countSZan(S, start, end)

        if zan == c:
            return S[start:end+1]
        #return
        #print len(S), S[11]

        for end in range(end+1, len(S)+1):

            if zan < c:
                e = S[end-1]

                if e in self.zan:

                    if e in self.szan:
                        self.szan[e] += 1
                    else:
                        zan += 1
                        self.szan[e] = 1

            #print start, end, zan, s, S[start:end]


            while zan == c:
                l = end - start
                if minlen == -1 or minlen > l:
                    minstart = start
                    minend = end
                    minlen = l

                s = S[start]

                #print start, end, zan, s, S[start:end]

                if s in self.szan:
                    self.szan[s] -= 1
                    if self.szan[s] == 0:
                        del self.szan[s]
                        zan-= 1
                start += 1

        minstr = ""
        if minlen > -1 :
            minstr = S[minstart:minend]

        return minstr


    def countTZan(self, T):
        self.zan = {}
        for i in T:
            self.zan[i] = 1
        return len(self.zan)


    def countSZan(self, S, start, end):

        for i in range(start, end):
            s = S[i]
            if s in self.zan:

                if s in self.szan:
                    self.szan[s] += 1
                else:
                    self.szan[s] = 1

        return len(self.szan)