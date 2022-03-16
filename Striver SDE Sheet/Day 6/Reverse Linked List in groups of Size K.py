#Question Link: https://takeuforward.org/data-structure/reverse-linked-list-in-groups-of-size-k/
#Solution Link (Python3): https://leetcode.com/submissions/detail/661149237/

#For complete code snippet and question, please refer leetcode link (https://leetcode.com/problems/reverse-nodes-in-k-group/)



class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        dummy = ListNode(None)
        dummy.next = head
        prev = curr = nxt = dummy
        
        count = 0
        
        while(curr.next is not None):
            count += 1
            curr = curr.next
        
        while(count >= k):
            curr = prev.next
            nxt = curr.next
            for i in range(k-1):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
            prev = curr
            count -= k
            
        return dummy.next
            
                
        
