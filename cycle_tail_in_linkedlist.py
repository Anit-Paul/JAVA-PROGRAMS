class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head

        slow = head
        if head == None:
            return None
        while fast and fast.next:
            slow = slow.next
            fast.val = None
            fast = fast.next.next
            if slow == fast:
                slow=head
                while(slow!=fast):
                    slow=slow.next
                    fast=fast.next
                return slow
        return None
