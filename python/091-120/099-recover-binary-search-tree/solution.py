__author__ = 'yinjun'

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        d = self.depth(root)
        for i in range(d):
            self.recover(root, None)
        return root

    def depth(self, root):
        if root == None:
            return 0
        else:
            left = 1 + self.depth(root.left)
            right = 1 + self.depth(root.right)
            if left>right:
                return left
            else:
                return right

    def recover(self, root, parent):
        if root == None:
            return
        print root.to_list()

        if root.left!= None and root.left.val > root.val and root.right == None:
            x = root.val
            root.val = root.left.val
            root.left.val = x
            print 'left', root.val, root.left.val
        elif root.right !=None and root.right.val < root.val and root and root.left==None:
            x = root.val
            root.val = root.right.val
            root.right.val = x
            print 'right', root.val, root.right.val
        elif root.left!= None and  root.right !=None and (root.left.val > root.right.val or root.left.val > root.val or root.right.val< root.val):
            a = [root.val, root.left.val, root.right.val]
            a.sort()
            root.left.val = a[0]
            root.val = a[1]
            root.right.val = a[2]
            print root.val, root.left.val, root.right.val
        elif parent !=None:
            #TODO: complete this algorigthm
            return
            # if root.left!= None and parent.val < root.left.val:
            #     x = parent.val
            #     parent.val = root.left.val
            #     root.left.val = x
            # elif root.right !=None and parent.val >

        self.recover(root.left, root)
        self.recover(root.right, root)



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def from_list(list):

        l = len(list)
        if l ==0:
            return None

        root = TreeNode(list[0])
        nodes = [root]
        pos = 0

        for i in range(1, l, 2):
            n = nodes[pos]
            pos += 1

            v = list[i]
            if v != '#':
                n.left = TreeNode(v)
                nodes.append(n.left)

            if i+1 < l:
                v = list[i+1]
                if v != '#':
                    n.right = TreeNode(list[i+1])
                    nodes.append(n.right)


        return root


    def to_list(self):
        self.list = []
        self.list.append(self.val)
        if self.left == None and self.right!=None:
            self.list.append('#')
        self.to_list2(self.left)
        self.to_list2(self.right)
        return self.list


    def to_list2(self, node):

        if node == None:
            return

        self.list.append(node.val)

        if node.left == None and node.right != None:
            self.list.append('#')

        self.to_list2(node.left)
        self.to_list2(node.right)

s = Solution()
root = TreeNode.from_list([2,'#',3,1])
#print root.to_list()
tree = s.recoverTree(root)
print tree.to_list()
