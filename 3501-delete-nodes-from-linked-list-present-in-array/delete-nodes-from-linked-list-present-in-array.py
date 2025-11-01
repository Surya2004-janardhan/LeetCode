# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        prev = ListNode(0)
        prev.next = head
        returN = prev
        nums = set(nums)
        while head:

            if head.val in nums:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next
        return returN.next

