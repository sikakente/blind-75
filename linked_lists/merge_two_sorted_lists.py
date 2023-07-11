# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = l3 = None

        while list1 and list2:
            if list1.val <= list2.val:
                if not l3:
                    head = l3 = list1
                    list1 = list1.next
                else:
                    l3.next = list1
                    list1 = list1.next
                    l3 = l3.next
            else:
                if not l3:
                    head = l3 = list2
                    list2 = list2.next
                else:
                    l3.next = list2
                    list2 = list2.next
                    l3 = l3.next

        if list1:
            if not l3:
                head = l3 = list1
            else:
                l3.next = list1

        if list2:
            if not l3:
                head = l3 = list2
            else:
                l3.next = list2

        return head