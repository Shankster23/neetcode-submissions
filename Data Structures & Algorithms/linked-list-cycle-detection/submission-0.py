# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head
        while(hare != None and hare.next != None and hare.next.next != None):
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                return True
        return False