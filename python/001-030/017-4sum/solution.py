class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):

        nums.sort();
        length = len(nums)
        self.result = []

        for i in xrange(length - 3):
            if i != 0 and nums[i] == nums[i - 1]:
				continue

            for j in xrange(i+1, length -2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue

                target2 = target - nums[i] - nums[j]
                self.twoSum(nums, target2, j+1, length, nums[i], nums[j])

        return self.result


    def twoSum(self, num, target, start, length, first, second):

        end = length - 1
        #print first, start, end
        while start < end:

            sum = num[start] + num[end]
            #print first, start, end, sum, target

            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                # sum == target:
                # return (start, end)
                self.result.append([first, second, num[start], num[end]])

                nstart = start + 1
                while nstart < end and num[nstart] == num[start]:
                    nstart += 1
                start = nstart

                nend = end - 1
                while nend > start and num[nend] == num[end]:
                    nend -= 1
                end = nend

        #return None