
class HashTable:
    
    def __init__(self):
        self.capacity=10
        self.table=[[] for _ in range(self.capacity)]
        self.size=0
        
    def hash_index(self,userid):
       
           
       return userid%self.capacity
    
    def insert(self, userObject):
       userid = userObject.userid
       if self.search(userid) is not None:
           print("User ID already exists. Please use a different User ID.")
           return False
       self.table[self.hash_index(userid)].append(userObject)
       self.size += 1
       if (self.size / self.capacity) > 0.75:
           self._resize()
       return True

    def _resize(self):
       old_table = self.table
       self.capacity *= 2
       self.table = [[] for _ in range(self.capacity)]
       self.size = 0
       for bucket in old_table:
           for user in bucket:
               self.table[self.hash_index(user.userid)].append(user)
               self.size += 1
                       
         
                   
    def search(self,userid):
       index = self.hash_index(userid)
       bucket = self.table[index]
       for user in bucket:
           if user.userid == userid:
               return user
       return None
               
    def delete(self, userid):

       index = self.hash_index(userid)
       bucket = self.table[index]
       for i, user in enumerate(bucket):
             if user.userid == userid:
                 bucket.pop(i)
                 self.size -= 1
                 return True
       return False
       
    

    def display(self):
        result = []
        for bucket in self.table:
            for user in bucket:
                result.append(user)
        if result:
            for user in result:
                print(user.__dict__)
        else:
            print("No users found")
        return result
    