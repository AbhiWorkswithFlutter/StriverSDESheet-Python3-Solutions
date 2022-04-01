#Question Link: https://takeuforward.org/data-structure/job-sequencing-problem/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=6e1025da27f71f81bd52b6cd72249e55&pid=701367&user=tiabhi1999


#For complete code snippet and question, please refer Gfg link (https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#)
  
class Solution:
    
    def JobScheduling(self,Jobs,n):
        Jobs= sorted(Jobs, key= lambda Jobs: Jobs.profit, reverse= True)
        deadline= sorted(Jobs, key= lambda Jobs: Jobs.deadline , reverse = True)
        maxDeadline = deadline[0].deadline
        slots = [0]*(maxDeadline+1)
        res = 0
        a = []
        profit = 0
        for job in Jobs:
            if job.deadline <= maxDeadline and slots[job.deadline] != 1:
                slots[job.deadline] = 1
                profit += job.profit
                res += 1
            else:
                for i in range(job.deadline , 0, -1):
                    if slots[i] != 1:
                        slots[i] = 1
                        profit += job.profit
                        res += 1
                        break
        return res, profit
        
        
