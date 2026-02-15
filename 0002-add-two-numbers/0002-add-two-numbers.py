# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reminder = 0
        head = dummy = ListNode()
        while l1 or l2:
            #print(l1.val, l2.val, reminder)
            csum = reminder
            if l1:
                csum += l1.val
                l1 = l1.next
            if l2:
                csum += l2.val
                l2 = l2.next
            reminder = csum // 10
            csum = csum % 10
            head.next = ListNode(val=csum)
            head = head.next
            
        if reminder:
            head.next = ListNode(val=reminder)
    
        return(dummy.next)

        
             
