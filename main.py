from user import user
from hash import hash
users=user()
choice=int(input("Enter 1 to add user and 2 to exit : "))
match choice:
    case 1:
        name=input("Enter Name : ")
        age=int(input("Enter age : "))
        gender=input("Enter gender : ")
        height=float(input("Enter height : "))
        weight=float(input("Enter weight : "))
        bmi=float(input("Enter BMI : "))
        goal_weight=float(input("Enter goal weight : "))
        users.insert(name,age,gender,height,weight,bmi,goal_weight)
    
    case 2: 
        exit()