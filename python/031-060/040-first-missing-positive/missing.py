class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):

        l = len(A)
        missing = 1

        if(l>0):
            maxi = A[0]
            for i in range(1, l):
                if A[i] > maxi:
                    maxi = A[i]

            d = [ 0 ] * maxi
            #print  mini, maxi, A, d


            print A, d
            for i in range(0, l):
                if A[i] > 0:
                    d[A[i]-1] = 1

            print maxi, d
            find = False
            for i in range(0, maxi):
                if d[i] == 0 :
                    missing = i + 1
                    find = True
                    break
            if find == False:
                missing= maxi+1

        return missing


s = Solution()

print s.firstMissingPositive([1,1])
print s.firstMissingPositive([1,2,0])
print s.firstMissingPositive([3,4,-1,1])
print s.firstMissingPositive([98,93,95,10,91,4,90,88,56,84,65,62,83,80,78,60,73,77,76,29,63,12,57,17,69,68,50,11,31,33,8,42,38,7,0,37,48,26,20,44,46,43,52,51,47,18,49,58,2,39,30,81,22,55,36,40,15,27,21,32,64,41,53,19,28,24,9,25,3,59,66,82,61,70,23,34,71,54,74,-1,1,45,14,79,5,35,13,72,75,85,87,6,16,86,67,89,94,92,96,97])
