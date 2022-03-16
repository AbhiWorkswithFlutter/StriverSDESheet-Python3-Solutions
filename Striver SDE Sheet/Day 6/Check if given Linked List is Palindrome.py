#Question Link: https://takeuforward.org/data-structure/check-if-given-linked-list-is-plaindrome/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=9b2badd244a3197cef4fefec5839268a&pid=700391&user=tiabhi1999

#for complete code snippet please refer Gfg question (https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1/)

class Solution:
    def reverse(self, head):
        if not head:
            return
        prev = None
        curr = head
        nex = None
        
        while(curr):
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev
    def middleele(self, head):
        if not head:
            return
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow
            
    def isPalindrome(self, head):
        if not head:
            return
        mid = self.middleele(head)
        end = self.reverse(mid)
        while(head and end):
            if head.data == end.data:
                head = head.next
                end = end.next
            else:
                return 0
                break
        return 1
