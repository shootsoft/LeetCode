class Solution:


    def findSubstring(self, S, L):
        n = len(L) #num words
        w = len(L[0])  #length of each word
        t = n*w    # total length

        hashsum = sum([hash(x) for x in L])
        h = [hash(S[i:i+w])*(S[i:i+w] in L) for i in xrange(len(S)-w+1)]
        return [i for i in xrange(len(S)-t+1) if sum(h[i:i+t:w])==hashsum]
