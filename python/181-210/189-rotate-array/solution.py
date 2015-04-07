class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        l = len(nums)
        if k>=l:
            return None
        else:
            p = l - k

            
            return nums[p:] + nums[0:p]