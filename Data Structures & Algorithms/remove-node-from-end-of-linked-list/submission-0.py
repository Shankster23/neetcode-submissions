# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        first_traversal = head
        second_traversal = head
        start = head
        prev = ListNode()
        prev.next = second_traversal
        while first_traversal != None:
            first_traversal = first_traversal.next
            count+=1
        for i in range(count - n):
            second_traversal = second_traversal.next
            prev = prev.next
        prev.next = prev.next.next
        if count - n == 0:
            return prev.next
        return head