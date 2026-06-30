from hash import hash
hashing=hash()
class user:

    def insert(self,name , age, gender, height, weight, bmi, goal_weight):
       
       hashing.logic(name)
       hashing.table[hashing.calculation].append([name,age,gender,height,weight,bmi,goal_weight])
       hashing.size+=1  
       print("User added successfully")
       print(hashing.table)
    

