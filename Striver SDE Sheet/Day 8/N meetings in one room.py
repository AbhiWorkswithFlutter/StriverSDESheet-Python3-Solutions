#Question Link: https://takeuforward.org/data-structure/n-meetings-in-one-room/
#Solution (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=6ec6f3d43a5c54deed9153827cbfe17f&pid=701364&user=tiabhi1999

#For complete code snippet and question, please refer the GFG Link (https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1#)


def maximumMeetings(self,n,start,end):
        meeting = []
        
        for i in range(n):
            ele = [start[i], end[i], i]
            meeting.append(ele)
            
        meeting = sorted(meeting, key = lambda x: x[1])
       
        res = []
        res.append(meeting[0])
        
        for i in range(1, len(meeting)):
            if res[-1][1] < meeting[i][0]:
                #If you want to print the meeting numbers or start and end time, append accordingly
                res.append(meeting[i])
       
        return len(res)
