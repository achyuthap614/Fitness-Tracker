from workout import workout_manager
from hash import HashTable
class User:
    def __init__(self,userid,name,age,gender,height,weight,bmi,goal_weight):
        self.userid=userid
        self.name=name
        self.age=age
        self.gender=gender
        self.height=height
        self.weight=weight
        self.bmi=bmi
        self.goal_weight=goal_weight
        self.workout_manager=workout_manager()
class UserManager:
   
   def __init__(self):
   
     self.user_table=HashTable()


   def add_user(self,userid,name,age,gender,height,weight,bmi,goal_weight):
       user = User(userid,name,age,gender,height,weight,bmi,goal_weight)
       return self.user_table.insert(user)

   def search(self, userid):

        return self.user_table.search(userid)

   def delete(self, userid):
        return self.user_table.delete(userid)

   def display_users(self):
        return self.user_table.display()
        
