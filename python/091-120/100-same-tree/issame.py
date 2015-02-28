__author__ = 'yinjun'


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):

        if p==None and q==None or p!=None and q!=None and p.left == None and q.left == None and p.right == None and q.right == None and p.val == q.val:
            return True
        elif p==None or q==None:
            return False
        elif p!=None and q!=None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)