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
        len=1
        lnode=head
        while lnode.next is not None:
            lnode=lnode.next
            len=len+1
        k=k%len
        while (k>0):
            if fast.next is not None:
                fast=fast.next
                k=k-1
                # elif fast.next is None:
                #     fast=head
                # k=k-1
        # else:
        #     fast=fast
        #return fast
        if fast==head:
            return head
        else:
            while fast.next is not None:
                slow=cur
                cur=cur.next
                fast=fast.next
            fast.next=head
            slow.next=None
            return cur

head = Node(1)
list2 =Node(2)
head.next = list2

obj = Solution()

result = obj.rotateRight(head,3)
print (result.val)



