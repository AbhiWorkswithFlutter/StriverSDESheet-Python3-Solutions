#Question Link: https://takeuforward.org/data-structure/flattening-a-linked-list/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=86a214183d7dcc664d9cc9cd921fc72a&pid=700192&user=tiabhi1999

#For the complete code snippet and question, please refer GFG link (https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1#)


def mergeTwoLists(a, b):
    
    temp = Node(0)
    res = temp
    
    while(a is not None and b is not None): 
        if(a.data < b.data):
            temp.bottom = a
            temp = temp.bottom
            a = a.bottom 
    
        else:
            temp.bottom = b
            temp = temp.bottom
            b = b.bottom
        
    
    
    if(a is not None):
        temp.bottom = a
    else:
        temp.bottom = b
    
    return res.bottom

def flatten(root):
    if (root is None or root.next is None):
        return root
  
    root.next = flatten(root.next)
    root = mergeTwoLists(root, root.next); 
  
    return root
    
