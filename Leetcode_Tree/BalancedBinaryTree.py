#Not a good solution...research for better solutions
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            ans = 0
        else:
            if root.left is not None and root.right==None:
                ans=self.minDepth(root.left)+1
            elif root.left == None and root.right is not None:
                ans=self.minDepth(root.right)+1
            else:
                ans=min(self.minDepth(root.left), self.minDepth(root.right)) +1
        return ans
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            ans=0
        else:
            ans=max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        return ans
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            result=True
        elif root.left==None or root.right==None:
            result=self.maxDepth(root)<3
        elif self.isBalanced(root.left)==True and self.isBalanced(root.right)==True:
            result=abs(self.maxDepth(root.left)-self.maxDepth(root.right))<2
        else:
            result=False#self.isBalanced(root.left) and self.isBalanced(root.right)
        return result