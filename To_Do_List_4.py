import sys
import time

def Task():

    Task_list = []

    print("---WELCOME TO OUR TO DO LIST!---")

    total_task=int(input("Enter How many task you want to enter :\n"))
    for i in range(1,total_task+1):
        task_name=input(f"Enter your {i} Task : \n")
        Task_list.append(task_name)

    print(f"Today's Tasks are \n {Task_list}")

    while True:
        Operation = int(input("Enter Operation :\n 1 - Add Task \n 2 - Update Task \n 3 - Delete Task \n 4 - View Task\n 5 - Exit Task\n"))

        if (Operation == 1):
          add = input("Enter what u want to add : \n")
          Task_list.append(add)   
          print("Your Task has been Successfully Added\n")

        elif (Operation == 2):
          Update_Val = input("Enter the Task name what u want to Update : \n")
          if Update_Val in Task_list:
             up = input("Enter new Task : ")
             ind = Task_list.index(Update_Val)
             Task_list[ind] = up
          print("Your Task has been Successfully Updated\n")

        elif(Operation == 3):
          delete = input("Enter what u want to Delete : \n")

          if delete in Task_list:
            Task_list.remove(delete)   
            print("Your Task has been Successfully Deleted\n")

        elif(Operation == 4):
          print(f"Your Tasks are {Task_list}\n")
          time.sleep(3)

        elif(Operation==5):
           print("Closing the program....\n")
           sys.exit()


Task()
