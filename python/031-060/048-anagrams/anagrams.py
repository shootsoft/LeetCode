class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):

        d = {}
        c = {}
        l = len(strs)

        if(l==1):
            return []

        for i in range(l):
            key = list(strs[i])
            key.sort()
            key = str(key)
            if key in d:
                d[key].append(strs[i])
                c[key]+=1
            else:
                d[key] = [strs[i]]
                c[key] = 1

        r = []
        for k,v  in d.items():
            if c[k] > 1:
                r += v
        return r


s = Solution()
print s.anagrams(["tea","and","ate","eat","den"])

