import datetime

class Solution:
    # @return an integer
    def threeSumClosest(self, nums, target):
        #starttime = datetime.datetime.now()
        nums.sort()
        l = len(nums)

        m = 0
        #r =
        for x in range(l):
            if nums[x] >0 and m == 0:
                m = x

        mintarget = None
        mind = None

        for x in range(l):

            if x >0 and nums[x] == nums[x-1]:
                continue

            for y in range(x+1, l):

                if y > x+1 and nums[y] == nums[y-1]:
                    continue

                cur = nums[x]+nums[y]

                #if cur > target:
                #    break

                zs = y+1
                ze = l #last


                if cur < 0 and zs < m:
                    zs = m

                #find = False
                for z in range(zs, ze):

                    if z > zs and nums[z] == nums[z-1]:
                        continue

                    d = cur + nums[z]
                    n = self.abs( d - target )
                    if n == 0:
                        print nums[x],nums[y],nums[z]
                        return d
                    elif mintarget == None:
                        mintarget = n
                        mind = d
                    elif d < mind:
                        mintarget = n
                        mind = d

        return d

    def abs(self, n):
        if n<0:
            return n*-1
        else:
            return n

s = Solution()
print s.threeSumClosest([-1,2,1,-4], 1)

starttime = datetime.datetime.now()
print s.threeSumClosest([-84,-3,45,-85,-100,-75,60,-82,32,-11,18,-37,-38,58,-13,-56,24,-35,93,-74,22,24,78,-90,87,-93,42,-26,-15,85,98,-57,-65,-22,10,-50,76,-81,12,62,-37,35,-49,92,-45,-91,48,30,-72,70,14,80,60,76,97,36,58,-44,-65,-3,77,-52,-74,3,100,-59,-59,2,-65,-22,82,-60,-61,-13,-5,-35,43,-39,-34,-95,-82,-46,59,-91,93,-85,-36,80,-14,-22,-42,-35,77,0,-83,78,-15,-70,-38,-97,-38,-70,-58,36,8,24,-83,-34,66,2,-96,44,36,50,5,36,94,83,55,56,-43,-46,72,-17,-81], -50)
endtime = datetime.datetime.now()
print (endtime - starttime)

