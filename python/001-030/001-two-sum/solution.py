class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):

        l = len(num)
        dnum = {}

        for i in range(l):
            dnum[num[i]] = 1

        for i in range(l):
            n = target - num[i]

            if n in dnum:
                e = num.index(n)
                if e!=i:
                    if e>i:
                        return (i+1, e+1)
                    else:
                        return (e+1, i+1)


        #[-1, -2, -3, -4, -5], -8
        #[-7, -6, -5, -4, -3]


        #[3,2,4], 6
        #[3,4,2]

        #[-3, 4, 3, 90], 0
        #[3, -4, -3, -90]


    #def find(self, num, target):
