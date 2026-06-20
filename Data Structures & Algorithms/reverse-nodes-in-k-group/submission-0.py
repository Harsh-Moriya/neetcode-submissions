# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        n = len(nodes)

        for i in range(0, n, k):
            if i + k <= n:
                nodes[i:i + k] = reversed(nodes[i:i + k])

        dummy = ListNode(0)
        curr = dummy
        for node in nodes:
            curr.next = node
            curr = curr.next

        curr.next = None

        return dummy.next