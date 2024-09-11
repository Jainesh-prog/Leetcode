# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        
        # Traverse the list
        while head is not None:
            # Check if the value is already a float (indicating we've visited this node)
            if isinstance(head.val, float):
                return True  # Cycle detected

            # Modify the value by adding 0.1 to mark it as visited
            head.val += 0.1
            head = head.next

        return False 


            
        