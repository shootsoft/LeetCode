class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):

        d = dict()
        l = len(num)
        m = l / 2
        for i in range(l):
            n = num[i]
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1

                if d[n] > m:
                    return n
        if l >0:
            maj = None
            max = 0
            for (k,v) in  d.items():
                if maj == None or v>max:
                    maj = k
                    max = v

            return maj
        else:
            return None