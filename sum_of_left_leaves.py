class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        
        def isLeaf(node):
            return node is not None and not node.left and not node.right
        
        total = 0
        if root.left and isLeaf(root.left):
            total += root.left.val
        else:
            total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)
        return total
