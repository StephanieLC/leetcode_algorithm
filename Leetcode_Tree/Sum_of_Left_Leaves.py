class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        if root:
            l, r = root.left, root.right
            print "root value"
            print root.val
            if l:
                print 'left child'
                print l.val
            if r:
                print 'right child'
                print r.val
            if l is not None and (l.left or l.right) is None:
                ans += l.val
                print "the value"
                print ans
            ans += self.sumOfLeftLeaves(l) + self.sumOfLeftLeaves(r)
        return ans

root = TreeNode(3)
l1 = TreeNode(9)


root.left = l1


l2_left = TreeNode(30)
l3 = TreeNode(10)


l1.left = l2_left
l2_left.left = l3


r1 = TreeNode(20)
root.right = r1
l2 = TreeNode(15)
r1.left = l2
r2 = TreeNode(7)
r1.right = r2

obj = Solution()
result = obj.sumOfLeftLeaves(root)
print(result)
