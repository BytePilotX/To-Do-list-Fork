def Task():
    Task_list=[]

    print("---WELECOM TO OUR TO DO LIST---")

    total_task=int(input("Enter How many task you want to enter :"))
    for i in range(1,total_task+1):
        task_name=input(f"Enter your {i} Task : ")
        Task_list.append(task_name)

    print(f"Your, Today's Tasks are \n {Task_list}")

    while True:
        Operation=int(input("Enter Operation :\n 1 - Add Task \n 2 - Update Task \n 3 - Delete Task \n 4 - View Task\n 5 - Exit Task"))

        if(Operation==1):
          add = input("Enter what u want to addd : ")
          Task_list.append(add)   
          print(f"Your Task has been Successfully Added")

        elif(Operation==2):
          Update_Val = input("Enter the Task name what u want to Update : ")
          if Update_Val in Task_list:
             up = input("Enter new Task : ")
             ind = Task_list.index(Update_Val)
             Task_list[ind] = up
          print(f"Your Task has been Successfully Updated")

        elif(Operation==3):
          delete = input("Enter what u want to Delete : ")

          if delete in Task_list:
            Task_list.remove(delete)   
            print(f"Your Task has been Successfully Deleted")

        elif(Operation==4):
          print(f"Your Tasks are {Task_list}")

        elif(Operation==5):
           print("Closing the program....")
           break

Task()