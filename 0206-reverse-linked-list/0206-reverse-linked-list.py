# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # The recursive solution is not efficient as It will have addition storage
        # for each node in stack during each recursive call.
        # def _rec(cur, prev=None):
        #     # Base case
        #     if not cur:
        #         return(prev)
        #    
        #     nxt = cur.next
        #     cur.next = prev
        #     return(_rec(nxt, cur))
        #
        # return(_rec(head))
        

        prev = None
        curr = head
        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        return(prev)
