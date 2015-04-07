__author__ = 'yinjun'

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):

        if root == None:
            return False

        v = sum - root.val

        #print v

        if v == 0 and root.left == None and root.right == None:
            return True
        else:

            return self.hasPathSum(root.left, v) or  self.hasPathSum(root.right, v)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(-2)
root.right = TreeNode(-3)
s = Solution()
print s.hasPathSum(root, -5)