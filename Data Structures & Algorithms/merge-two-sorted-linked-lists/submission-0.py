# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        
        if list1 == None:
                return list2
        elif list2 == None:
            return list1
        if(list1.val <= list2.val):
            res = ListNode(list1.val)
            list1 = list1.next
        elif(list2.val <= list1.val):
            res = ListNode(list2.val)
            list2 = list2.next
        begin = res
        dummyNode = ListNode(None, begin)
        while(list1 != None and list2 != None):
            if(list1.val <= list2.val):
                res.next = ListNode(list1.val)
                res = res.next
                list1 = list1.next
            elif(list2.val <= list1.val):
                res.next = ListNode(list2.val)
                res = res.next
                list2 = list2.next
        if list1 == None:
            res.next = list2
        elif list2 == None:
            res.next = list1
        return dummyNode.next