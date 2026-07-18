# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        carry = 0
        head = None
        while s1 or s2:
            csum = carry
            if s1:
                csum += s1.pop()
            if s2:
                csum += s2.pop()
            
            carry = csum // 10
            csum = csum % 10

            tmpNode = ListNode(val=csum)
            tmpNode.next = head
            head = tmpNode
        if carry:
            tmpNode = ListNode(val=carry)
            tmpNode.next = head
            head = tmpNode
        return(head)