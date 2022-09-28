# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        li = []
        cur = head
        
        while cur:
            li.append(cur)
            cur = cur.next
        
        if len(li) == n:
            return head.next
        elif n == 1:
            li[-2].next = None
        else:
            li[-n - 1].next = li[-n + 1]
            
        return head