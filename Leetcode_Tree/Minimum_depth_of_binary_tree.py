class TreeNode(object):
    def __init__(self, root):
        self.val = root
        self.left = None
        self.right = None

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

root = TreeNode(3)
l1 = TreeNode(9)


root.left = l1
#
#
# l2_left = TreeNode(30)
# l3 = TreeNode(10)
#
#
# l1.left = l2_left
# l2_left.left = l3
#
#
# r1 = TreeNode(20)
# root.right = r1
# l2 = TreeNode(15)
# r1.left = l2
# r2 = TreeNode(7)
# r1.right = r2

obj = Solution()
result = obj.minDepth(root)
print(result)
