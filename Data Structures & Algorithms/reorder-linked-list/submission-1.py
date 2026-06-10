# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        # When fast reaches the end slow will be at the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Save the second list's head
        second = slow.next
        # Break the list into two
        slow.next = None

        # Reverse the second list
        prev, curr = None, second

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # Get the new head for the second list
        second = prev

        # Merge the lists
        # Use second lists head as the condition because either both lists will end at the same time or second will end first
        while second:
            nxt1, nxt2 = head.next, second.next
            head.next = second
            second.next = nxt1
            head = nxt1
            second = nxt2