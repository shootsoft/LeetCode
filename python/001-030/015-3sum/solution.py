class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):

        self.result = []
        num.sort()
        length = len(num)
        #print num
        for i in range(0, length-2):
            #print i
            if i>0 and num[i-1] == num[i]:
                #print 'skip ', i
                continue

            self.twoSum(num, 0 - num[i], i+1, length)

        return self.result

    def twoSum(self, num, target, start, length):

        end = length - 1
        first = num[start - 1]
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
                self.result.append([first, num[start], num[end]])

                nstart = start + 1
                while nstart < end and num[nstart] == num[start]:
                    nstart += 1
                start = nstart

                nend = end - 1
                while nend > start and num[nend] == num[end]:
                    nend -= 1
                end = nend

        #return None