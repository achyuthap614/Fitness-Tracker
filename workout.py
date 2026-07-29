class Workout:
    def __init__(self,date,steps,calories_burnt,workout_time,workout_type,heart_rate,distance_walked):
        self.date=date
        self.steps=steps
        self.calories_burnt=calories_burnt
        self.workout_time=workout_time
        self.workout_type=workout_type
        self.heart_rate=heart_rate
        self.distance_walked=distance_walked
        self.next=None
        self.prev=None
        
    def __repr__(self):
        return (f"Workout(date={self.date!r}, steps={self.steps}, "
                f"calories_burnt={self.calories_burnt}, time={self.workout_time}, "
                f"type={self.workout_type}, hr={self.heart_rate}, "
                f"distance={self.distance_walked})")

    def __str__(self):
        return self.__repr__()
        
class WorkoutManager:
    def __init__(self):
        self.head=None
        self.tail=None

    def add_workout(self,date,steps,calories_burnt,workout_time,workout_type,heart_rate,distance_walked):
        new_workout=Workout(date,steps,calories_burnt,workout_time,workout_type,heart_rate,distance_walked)
        if self.head is None:
            self.head=new_workout
            self.tail=new_workout
        else:
            self.tail.next=new_workout
            new_workout.prev=self.tail
            self.tail=new_workout

    def display_workout(self):
        if self.head==None:
            print("No workouts added")
            return
        temp=self.head
        while temp is not None:
            print(str(temp))
            temp=temp.next
        return    
    def search_workout(self,search):
        temp=self.head
        while temp:
            if search==temp.date:
                print("Found",str(temp))
            
                return temp
            temp=temp.next
        return "Not found"


    def delete_workout(self,search):
        temp=self.head
        if temp is None:
            return "Not found"
        if search==self.head.date==self.tail.date:
            print("Deleted : " ,str(temp))
            self.head=None
            self.tail=None
            temp=None
            return
        if search==temp.date:
            print("Deleted : " ,str(temp))
            self.head=temp.next
            if self.head:
                self.head.prev=None
            temp=None
            print("Deleted")
            return 
        
        while temp:
            if search==temp.date:
                print("Deleted : " ,str(temp))
                
                temp.prev.next=temp.next
                if temp.next is not None:
                    temp.next.prev=temp.prev
                    temp=None
                    print("Deleted")
                    return 
                
                if temp==self.tail:
                    self.tail=temp.prev
                    temp=None
                    print("Deleted")
                    return 


            temp=temp.next
        return "Not found"
        
    