# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # No need to reorder if the list has 0 or 1 node

        odd = head
        even = head.next
        even_head = even  # To connect at the end of the odd list

        while even and even.next:
            odd.next = even.next  # Link current odd to the next odd node
            odd = odd.next        # Move odd pointer forward
            even.next = odd.next  # Link current even to the next even node
            even = even.next      # Move even pointer forward

        odd.next = even_head  # Connect the end of odd list to the head of even list
        return head

        