# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return

        queue = deque()
        stack = deque()
        iterator = head
        while iterator:
            queue.append(iterator)
            stack.append(iterator)
            iterator = iterator.next

        for i in range(len(queue)//2):
            front = queue.popleft()
            back = stack.pop()
            
            front.next = back
            
            if queue:
                next_front = queue[0]  # peek
                back.next = next_front

        # Handle any remaining node for odd-length lists
        if queue:
            queue[0].next = None