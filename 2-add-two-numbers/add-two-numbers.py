# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        create = dummy
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            temp = val1+val2+carry
            if temp >9:
                add = temp  % 10
                carry = temp//10
            else:
                add = temp
                carry = 0
            
            create.next = ListNode(add)
            create = create.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            create.next = ListNode(carry)
        return dummy.next