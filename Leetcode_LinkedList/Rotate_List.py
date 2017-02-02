class Node:
    def __init__(self, item):
        self.val = item
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k==0:
            return head
        slow=head
        cur=slow.next
        fast=head
        if k>0 and fast.next is not None:
            fast=fast.next
            k=k-1
        elif k>0 and fast.next is None:
            fast=head
            k=k-1
        return fast

head = Node(1)
list2 =Node(2)
head.next = list2

obj = Solution()

result = obj.rotateRight(head,3)



