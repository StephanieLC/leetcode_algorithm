class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def RootPathSum(root, sum):
            if root==None:
                return 0
            res=(sum==root.val)
            res+=RootPathSum(root.left,sum-root.val)
            res+=RootPathSum(root.right,sum-root.val)
            return res
        if root==None:
            return 0
        ans=RootPathSum(root,sum)
        ans+=RootPathSum(root.left,sum)
        ans+=RootPathSum(root.right,sum)
        return ans