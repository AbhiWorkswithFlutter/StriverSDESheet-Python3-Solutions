#Question Link: https://takeuforward.org/data-structure/starting-point-of-loop-in-a-linked-list/
#Solution Link (Python3): https://leetcode.com/submissions/detail/657107729/

#For the complete code snippet, please refer the leetcode question (https://leetcode.com/problems/linked-list-cycle-ii/)

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow = fast = temp = head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while(slow!=temp):
                    slow = slow.next
                    temp = temp.next
                return temp
        return None
