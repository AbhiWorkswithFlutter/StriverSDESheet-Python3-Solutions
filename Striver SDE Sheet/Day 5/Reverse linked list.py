#Question Link: https://takeuforward.org/data-structure/reverse-a-linked-list/
#Solution Link (Python3): https://leetcode.com/submissions/detail/656741545/

#refer leetcode link for complete code snippet (https://leetcode.com/problems/reverse-linked-list/)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        prev = None
        curr = head
        nxt = None
        
        while(curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
