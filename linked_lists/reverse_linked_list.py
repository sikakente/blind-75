# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r = p = None
        q = head
        reversed_head = None

        while q:
            r = p
            p = q
            q = q.next
            p.next = r

            if q is None:
                reversed_head = p

        return reversed_head
