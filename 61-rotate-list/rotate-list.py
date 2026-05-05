# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=head
        d=head
        g=head
        l=[]
        if head is None:return
        while n:
            l.append(n.val)
            n=n.next
        n=len(l)
        
        if k>n:
            
            k=k%n
            
        print(k)    
        l3=l[:n-k]
        l2=l[n-k:(n-k)+k]
        # print(l2)
        # l2=l2[::-1]
        l1=l2+l3 
        # print(l2)
        # print(l3)
        i=0
        while d:
            d.val=l1[i]
            d=d.next
            i+=1
        return g