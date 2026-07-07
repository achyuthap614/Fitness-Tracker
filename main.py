from user import UserManager

if __name__=="__main__":
    users=UserManager()
    while True:
        choice=int(input("1.Register User\n2.Search User\n3.Delete User\n4.Display User\n5.Login\n6.Exit"))
        match choice:
            case 1:
                name=input("Enter Name : ")
                age=int(input("Enter age : "))
                gender=input("Enter gender : ")
                height=float(input("Enter height : "))
                weight=float(input("Enter weight : "))
                bmi=float(input("Enter BMI : "))
                goal_weight=float(input("Enter goal weight : "))
                userid=int(input("Enter User ID : "))
                users.add_user(userid,name,age,gender,height,weight,bmi,goal_weight)
            
            case 2:
                search_userid=int(input("Enter the User ID to be searched : "))
                user = users.search(search_userid)
                if user is None:
                    print("User not found")
                else:
                    print(user.__dict__)

            case 3:
                delete_userid=int(input("Enter the User ID to be deleted : "))
                result = users.delete(delete_userid)
                if result:
                    print("Deleted")
                else:
                    print("User not found")
            
            case 4:
                users.display_users()
            
            case 5: 
                login=int(input("Enter UserID : "))
                login_user=users.search(login)
                if login_user is not None:
                    print(f"Welcome Back {login_user.name} ")
                    while True:
                        login_choice=int(input("1.Add Workout\n2.View Workout History\n3.Logout"))
                        match login_choice:
                            case 1:
                                date=int(input("Enter Date : "))
                                steps=int(input("Enter Steps Walked : "))
                                calories_burnt=int(input("Enter Calories Burnt"))
                                workout_time=int(input("Enter Workout Time : "))
                                workout_type=int(input("Enter Workout Type : "))
                                heart_rate=int(input("Enter Heart Rate"))
                                distance_walked=int(input("Enter Distance Walked : "))
  
                                login_user.workout_manager.add_workout(date,steps,calories_burnt,workout_time,workout_type,heart_rate,distance_walked)

                            case 2:
                                login_user.workout_manager.display_workout()

                            case 3:
                                exit()
                                