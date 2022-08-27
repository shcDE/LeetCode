# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        line = []
        
        while head:
            line.append(head.val)
            head = head.next
        
        return line == line[::-1]