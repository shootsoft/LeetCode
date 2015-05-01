class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):

        num.sort()
        #print num
        length = len(num)
        minDist = None
        minSum  = None

        for i in range(length-2):

            if i > 0 and num[i-1] == num[i]:
                continue


            target2 = target - num[i]

            sum = self.twoSumClosest(num, length, i+1, target2)
            #print target2, sum
            dist = target2 - sum
            if minDist == None or abs(dist) < abs(minDist):
                minDist = dist
                minSum = num[i] + sum
                #print 'ssss', i, num[i], sum, minSum

        return minSum

    def twoSumClosest(self, num, length, start, target):

        minDist = None
        minSum = None

        end = length - 1

        #print start, target

        while start < end:

            sum = num[start] + num[end]

            dist = sum - target
            if minDist == None or abs(dist) < abs(minDist):
                minDist = dist
                minSum = sum
                #print 'minSum', start, end, sum, target


            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:

                return sum


        return minSum


