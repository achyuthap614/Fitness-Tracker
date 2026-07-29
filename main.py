from user import UserManager
from csv_loader import csv_loaders
from linear_regression import LinearRegression

files = csv_loaders()

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
                        login_choice = int(input("1.Add Workout\n2.View Workout History\n3.Run Regression\n4.Logout"))
                        match login_choice:
                            case 1:
                                date = input("Enter Date : ")
                                steps = float(input("Enter Steps Walked : "))
                                calories_burnt = float(input("Enter Calories Burnt: "))
                                workout_time = input("Enter Workout Time : ")
                                workout_type = input("Enter Workout Type : ")
                                heart_rate = input("Enter Heart Rate: ")
                                distance_walked = input("Enter Distance Walked : ")

                                login_user.workout_manager.add_workout(date, steps, calories_burnt, workout_time, workout_type, heart_rate, distance_walked)

                                # persist this workout to Workouts.csv with user id
                                workout_row = [
                                    login_user.userid,
                                    date,
                                    steps,
                                    calories_burnt,
                                    workout_time,
                                    workout_type,
                                    heart_rate,
                                    distance_walked,
                                ]
                                files.save_to_csv(workout_row, filename="Workouts.csv")

                            case 2:
                                login_user.workout_manager.display_workout()

                            case 3:
                                # collect data from user's workout history
                                temp = login_user.workout_manager.head
                                X = []
                                y = []
                                while temp:
                                    try:
                                        X.append(float(temp.steps))
                                        y.append(float(temp.calories_burnt))
                                    except Exception:
                                        pass
                                    temp = temp.next

                                if len(X) < 2:
                                    print("Need at least 2 data points to run regression")
                                else:
                                    lr = LinearRegression()
                                    a, b = lr.fit(X, y)
                                    y_pred = lr.predict(X)
                                    error = lr.mse(y, y_pred)
                                    print(f"Fitted model: calories = {a:.4f}*steps + {b:.4f}")
                                    print(f"MSE: {error:.4f}")
                                    # plot and save
                                    imgfile = f"regression_user_{login_user.userid}.png"
                                    lr.plot_regression(X, y, y_pred, filename=imgfile)

                            case 4:
                                user_row = [
                                    login_user.userid,
                                    login_user.name,
                                    login_user.age,
                                    login_user.gender,
                                    login_user.height,
                                    login_user.weight,
                                    login_user.bmi,
                                    login_user.goal_weight,
                                ]
                                files.save_to_csv(user_row)
                                break
