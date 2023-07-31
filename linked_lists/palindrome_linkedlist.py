# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        q = []

        curr = head

        while curr:
            q.append(curr)
            curr = curr.next

        start, end = 0, len(q) - 1

        while start <= end:
            if q[start].val != q[end].val:
                return False
            start += 1
            end -= 1

        return True
