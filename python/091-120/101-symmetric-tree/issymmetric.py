__author__ = 'yinjun'

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):

        if root == None :
            return True
        else:
            return self.ifSymmetric(root.left, root.right)


    def ifSymmetric(self, tree1,  tree2):
        if tree1==None and tree2==None:
            return True
        elif tree1 == None or tree2 == None:
            return False

        if tree1.val != tree2.val:
            return False
        else:
            return self.ifSymmetric(tree1.left, tree2.right) and self.ifSymmetric(tree1.right, tree2.left)





class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


s = Solution()
