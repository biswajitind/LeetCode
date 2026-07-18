# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def _print(self,node):
        while node:
            print(node.val, "->", end="")
            node = node.next
        print("")

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = head = ListNode()
        while l1 or  l2:
            csum = carry
            if l1:
                csum += l1.val
                l1 = l1.next
            if l2:
                csum += l2.val
                l2 = l2.next

            carry = csum // 10
            csum = csum % 10                        
            
            head.next = ListNode(val=csum)
            head = head.next

        if carry:
            head.next = ListNode(val=carry)


    
        return(dummy.next)