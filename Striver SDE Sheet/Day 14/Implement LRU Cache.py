#Question Link: https://takeuforward.org/data-structure/implement-lru-cache/
#Solution (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=88c472891470c45f3e3cc3de6b72c663&pid=700366&user=tiabhi1999

#For complete code snippet and question, please refer the GFG Link (https://practice.geeksforgeeks.org/problems/lru-cache/1)


class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self,cap):
        self.cap = cap
        self.dict = collections.OrderedDict()
        

    #Function to return value corresponding to the key.
    def get(self, key):
        if self.dict.get(key) is not None:
            self.dict.move_to_end(key)
            return self.dict[key]
        else:
            return -1
        
        
    #Function for storing key-value pair.   
    def set(self, key, value):
        if self.dict.get(key) is not None:
            self.dict.move_to_end(key)
            self.dict[key] = value
        else:
            self.dict[key] = value
            
        if len(self.dict)>self.cap:
            self.dict.popitem(last=False)

            
