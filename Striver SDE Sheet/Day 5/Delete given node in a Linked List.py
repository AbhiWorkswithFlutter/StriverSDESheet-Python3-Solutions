#Question Link: https://takeuforward.org/data-structure/delete-given-node-in-a-linked-list-o1-approach/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=c084587714657e058c6115b8d0e5bcc2&pid=700161&user=tiabhi1999

#Refer GfG question for understanding the code snippet. (https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1/)

class Solution:
    def deleteNode(self,curr_node):
        if curr_node.next is not None:
            curr_node.data = curr_node.next.data
            curr_node.next = curr_node.next.next
            return curr_node
        return
        
        
            
       

