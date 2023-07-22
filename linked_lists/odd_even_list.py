class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        
        head_odd, head_even = head, head.next
        odd, even = head, head.next

        while odd and even:
            if odd.next:
                odd.next = odd.next.next
                if odd.next is not None:
                    odd = odd.next
            
            if even.next:
                even.next = even.next.next
                even = even.next
            else:
                even.next = None
                break
        
        odd.next = head_even

        return head_odd