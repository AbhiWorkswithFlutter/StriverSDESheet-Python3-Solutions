#Question Link: https://takeuforward.org/data-structure/m-coloring-problem/
#Solution (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=ad184867bc39a85f8eb335c5b110d370&pid=701374&user=tiabhi1999

#For complete code snippet and question, please refer the GFG link (https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1#)

def isSafe(node, graph, color, V, col):
    for i in range(V):
        if graph[node][i] == 1 and color[i] == col:
                return False
        
    return True
    


def solve(node, graph, color, V, k):
    if node == V:
        return True
    
    for i in range(1,k+1):
        if isSafe(node, graph, color, V, i):
            color[node] = i
            if solve(node+1, graph, color, V, k):
                return True
            color[node] = 0
 
    return False 


def graphColoring(graph, k, V):
   
    color = [0]*V
    if solve(0, graph, color, V, k):
        return True
    return False
