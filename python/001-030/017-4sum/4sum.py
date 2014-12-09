class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, nums, target):
        #starttime = datetime.datetime.now()
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

                #if y > x+1 and nums[y] == nums[y-1]:
                #    continue

                cur = nums[x]+nums[y]

                if cur > target:
                    break

                #find = False
                for z in range(y+1, l):

                    #if z > y+1 and nums[z] == nums[z-1]:
                    #    continue

                    cur = nums[x]+nums[y]+nums[z]

                    if cur > target:
                        break

                    for u in range(z+1, l):

                        #if u > z+1 and nums[u] == nums[u-1]:
                        #    continue

                        n = cur + nums[z]
                        if n == target:
                            #find = True
                            r[ind] = ([nums[x],nums[y],nums[z], nums[u]])
                            ind+=1
                            #last = z
                            #lastv = cur
                            break
                        elif cur > target:
                            break
                #if find:
                #    break

        #endtime = datetime.datetime.now()
        #print (endtime - starttime)
        return r.values()

s = Solution()
print s.fourSum([1,0,-1,0,-2,2], 0)