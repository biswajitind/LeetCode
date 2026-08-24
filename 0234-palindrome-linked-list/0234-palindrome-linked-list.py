# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Using slow and fast pointer determind the mid point. 
        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        # At this time we have slow pointer pointing to the mid ( or the right one of the two middle nodes.)
        # This node should point to Null and following nodes should reverse.

        prev = None
        cur = slow
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        tail = prev

        # Now we can check for palindrome
        while tail:
            if not head.val == tail.val:
                return(False)
            head = head.next
            tail = tail.next
        return(True)
