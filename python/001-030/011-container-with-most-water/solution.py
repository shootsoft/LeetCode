class Solution:
    # @return an integer
    def maxArea(self, height):

        left = 0
        right = len(height) - 1
        max = 0

        while left < right:

            h = height[left]

            if height[right] < h:
                h = height[right]

            s = ( right - left ) * h

            if s > max:
                max = s

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return max
