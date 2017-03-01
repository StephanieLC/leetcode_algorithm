class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        root=TreeNode(nums[len(nums)/2])
        root.left=self.sortedArrayToBST(nums[:len(nums)/2])
        root.right=self.sortedArrayToBST(nums[(len(nums)/2+1):])
        return root