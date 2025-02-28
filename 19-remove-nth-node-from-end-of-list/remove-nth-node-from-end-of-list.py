# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        target = length - n 
        if target == 0:
            return head.next
        prev,curr = None, head
        for _ in range(target):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return head
        