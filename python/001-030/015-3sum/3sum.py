import datetime

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, nums):

        #starttime = datetime.datetime.now()
        target = 0
        nums.sort()
        l = len(nums)

        m = 0
        r = {}
        for x in range(l):
            if nums[x] >0 and m == 0:
                m = x

        last = l
        lastv = None
        ind = 0
        for x in range(l):

            if x >0 and nums[x] == nums[x-1]:
                continue

            for y in range(x+1, l):

                if y > x+1 and nums[y] == nums[y-1]:
                    continue

                cur = nums[x]+nums[y]

                if cur > target:
                    break

                zs = y+1
                ze = last

                if lastv != None and cur < lastv:
                    zs = last
                    ze = l

                if cur < 0 and zs < m:
                    zs = m

                #find = False
                for z in range(zs, ze):

                    if z > zs and nums[z] == nums[z-1]:
                        continue

                    n = cur + nums[z]
                    if n == target:
                        #find = True
                        r[ind] = ([nums[x],nums[y],nums[z]])
                        ind+=1
                        last = z
                        lastv = cur
                        break
                    elif cur > target:
                        break
                #if find:
                #    break

        #endtime = datetime.datetime.now()
        #print (endtime - starttime)
        return r.values()

s = Solution()
#print s.threeSum([-1,0,1,2,-1,-4])
#print s.threeSum([-9,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,-7,-5,9,11,-1,1,3,-15,-5,11,-12,-4,-4,-2,-6,-10,-6,-6,0,2,-9,14,-14,-14,-9,-1,-2,-7,-12,-13,-15,-4,-3,1,14,3,-12,3,3,-10,-9,-1,-7,3,12,-6,0,13,4,-15,0,2,6,1,3,13,8,-13,13,11,11,13,14,-6])
#print s.threeSum([-10,5,-11,-15,7,-7,-10,-8,-3,13,9,-14,4,3,5,-7,13,1,-4,-11,5,9,-11,-4,14,0,3,-10,-3,-7,10,-5,13,14,-5,6,14,0,5,-12,-10,-1,-11,9,9,1,-13,0,-13,-1,4,0,-7,8,3,14,-15,-9,-10,-3,0,-15,-1,-2,6,9,11,6,-14,1,1,-9,-14,6,7,10,14,2,-13,-13,8,6,-6,8,-9,12,7,-9,-11,4,-4,-4,4,10,1,-12,-3,-2,1,-10,6,-13,-3,-1,0,11,-5,0,-2,-11,-6,-9,11,3,14,-13,0,7,-14,-4,-4,-11,-1,8,6,8,3])
#print s.threeSum([2,5,5,8,-7,-9,5,-1,-4,2,8,4,-6,-2,-2,9,-2,13,1,0,9,9,4,-13,13,3,-14,11,-5,-13,3,4,7,-15,-11,7,13,1,13,-14,11,-1,5,-10,12,11,14,-13,1,-8,3,-4,-14,14,-10,-15,-6,-9,3,-4,-7,-8,-15,8,-8,12,-8,13,-2,-9,14,-6,5,-3,-9,-6,-7,-10,-3,9,-2,7,-10,-9,-2,-5,13,7,-6,2,-12,-6,1,10,9,0,7,-13,-2,-9,-7,-2,-8,5,10,-1,6,-12,4,10,12,9,2,10,8,-15,12,6,-1,-9,-7,2])

starttime = datetime.datetime.now()
print s.threeSum(
[7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
)

endtime = datetime.datetime.now()
print (endtime - starttime)

#print s.threeSum([0,0,0])
#print [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
#print s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
