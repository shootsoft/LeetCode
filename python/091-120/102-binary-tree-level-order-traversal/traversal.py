__author__ = 'yinjun'

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):

        self.order = []
        self.length = 0

        self.addNode(0, root)

        return self.order

    def addNode(self, level, node):

        if node == None:
            return

        if self.length == level:
            self.order.append([])
            self.length+=1

        self.order[level].append(node.val)

        self.addNode(level + 1, node.left)
        self.addNode(level + 1, node.right)