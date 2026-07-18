# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _print(self, node):
        while node:
            print(node.val, " ", end="")
            node = node.next
        print("")

    def _reverse(self, node):
        head  = node
        nxtNode = node.next
        head.next = None

        while nxtNode:
            tmpNode = nxtNode
            nxtNode = nxtNode.next
            tmpNode.next = head
            head = tmpNode

        return(head)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1 = self._reverse(l1)
        l2 = self._reverse(l2)
        carry = 0
        dummy = head = ListNode()
        while l1 or l2:
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

        return(self._reverse(dummy.next))