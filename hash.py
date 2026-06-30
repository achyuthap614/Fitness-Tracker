class hash:
    
    def __init__(self):
        self.capacity=10
        self.table=[[] for _ in range(self.capacity)]
        self.size=0
        
    def logic(self,name):
       count=0
       for _ in name:
           count=count+ord(_)
       self.calculation=count%self.capacity
       load_factor=self.size/self.capacity
       if load_factor>0.75:
           print(load_factor)
           old_table=self.table
           self.capacity=self.capacity*2
           self.table=[[] for _ in range(self.capacity)]
           for i in old_table:
               
               for j in i:
                   
                       self.logic(j)
                       self.table[self.calculation].append(j)
                       
                   
                   

    
     
