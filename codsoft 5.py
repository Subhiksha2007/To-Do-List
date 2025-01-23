tasks=[]
#Function to add task
def add_task():
    task=input("Enter a new task : ")
    tasks.append(task)
    print("Task added successfully")
#Function to view task
def view_task():
    if len(tasks)==0:
        print("Tasks not available")
    else:
        print("List of tasks : ")
        for i,task in enumerate(tasks):
            print(f"{i*1}.{task}")
#Function for deleting task
def delete_task():
    choice=int(input("Enter the task number to delete: "))
    if 0<choice<=len(tasks):
        del tasks[choice-1]
        print("Task deleted successfully")
    else:
        print("Invalid task number")
def main():
    while True:
        print("\t\tTo Do List Application")
        print("1. Add task")
        print("2. View task")
        print("3. Delete task")
        print("4.Quit")
        option=int(input("Enter your choice : "))
        if option==1:
            add_task()
        elif option==2:
            view_task()
        elif option==3:
            delete_task()
        elif option==4:
            print("See You Later!")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
   
