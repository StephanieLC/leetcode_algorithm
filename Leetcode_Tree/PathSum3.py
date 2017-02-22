class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def RootPathSum(root, val):
            if not root:
                return 0
            res=(val==root.val)
            res+=RootPathSum(root.left,val-root.val)
            res+=RootPathSum(root.right,val-root.val)
            return res
        if not root:
            return 0
        ans=RootPathSum(root,sum)
        ans+=self.pathSum(root.left,sum)
        ans+=self.pathSum(root.right,sum)
        return ans