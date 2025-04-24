class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case
        if not head: return None
        
        # Dummy Node
        dummy = ListNode(0, head)

        # dup's initial value is a value that 
        # a node cannot have in this problem
        prev, cur = dummy, head
        dup = -101
        while cur.next:
            # If a duplicate is found, save that value
            if cur.val == cur.next.val:
                dup = cur.val
            
            # If the current node's value is dup
            # Remove the current node
            if cur.val == dup:
                prev.next = cur.next

            # If not just update prev to its next node                
            else:
                prev = prev.next

            cur = cur.next

        # Check the last node
        if cur.val == dup:
            prev.next = None
        
        return dummy.next
            