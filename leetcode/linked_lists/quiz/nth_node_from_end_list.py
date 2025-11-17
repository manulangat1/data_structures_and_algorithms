from typing import Optional
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = res = ListNode(0, head) 
        for _ in range(n): 
            head = head.next
        while head: 
            head = head.next
            res = res.next
        res.next = res.next.next 
        return dummy.head


SLL = Solution()
SLL.removeNthFromEnd([1,2,3,4,5], 2)