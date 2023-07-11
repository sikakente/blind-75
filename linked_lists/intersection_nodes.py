# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        def get_length(node):
            if not node:
                return 0
            current = node
            count = 0
            while current:
                count += 1
                current = current.next
            return count

        list1_len = get_length(headA)
        list2_len = get_length(headB)
        if list1_len == list2_len:
            longer_list, longer_len = headA, list1_len
            shorter_list, shorter_len = headB, list2_len
        else:
            (longer_len, longer_list) = max([(list1_len, headA), (list2_len, headB)], key=lambda x: x[0])
            (shorter_len, shorter_list) = min([(list1_len, headA), (list2_len, headB)], key=lambda x: x[0])

        while longer_len > shorter_len:
            longer_list = longer_list.next
            longer_len -= 1

        while longer_list and shorter_list:
            if longer_list is shorter_list:
                return longer_list
            longer_list = longer_list.next
            shorter_list = shorter_list.next

        return
