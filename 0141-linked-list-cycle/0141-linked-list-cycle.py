# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Fast and slow pointer method

        if not head:
            return(False)

        fast, slow = head, head.next

        while fast and slow:
            if fast.next:
                fast = fast.next
            else:
                return(False)
            if fast.next:
                fast = fast.next
            else:
                return(False)

            # Loop
            if fast == slow:
                return(True)

            if slow.next:
                slow = slow.next
            else:
                return(False)


