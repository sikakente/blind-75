# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # create a heap with all the elements in the list and their values
        node_heap = [(node.val, idx) for idx, node in enumerate(lists) if node]
        heapq.heapify(node_heap)

        # init new node to None
        head = current = None

        # for each element in the heap
        while node_heap:
            _, smallest_node_idx = heapq.heappop(node_heap)
            smallest_node = lists[smallest_node_idx]
            if head:
                current.next = smallest_node
                current = current.next
            else:
                head = current = smallest_node

            if smallest_node.next:
                lists[smallest_node_idx] = smallest_node.next
                heapq.heappush(node_heap, (smallest_node.next.val, smallest_node_idx))

        return head
