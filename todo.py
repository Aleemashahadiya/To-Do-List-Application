Task=[]
while True:
    print("Welcome to the To-Do List program")
    print("----------------- ---------------------")
    print("choose a function:")
    print("1=View Task")
    print("2=Add Task")
    print("3=Remove Task")
    print("4=Exit")
    print("----------------- -------------------")
    choice=int(input("Enter your choice(1-4):"))
    if choice==1:
        if not Task:
            print("Your Task is empty.")
        else:
            print("Your Task:")
            print("------------------")
            for i, task in enumerate(Task, start=1):
                print(i,"-",task)
    elif choice==2:
        New_Task=input("Enter the task to add:")
        Task.append(New_Task)
        print(f"Task added successfully!\nTask added: {New_Task}")
    elif choice == 3:
        if not Task:
            print("No tasks available to remove.")
        else:
            Remove_Task = int(input("Enter the task number to remove: "))
            if 0 < Remove_Task <= len(Task):
                Removed_item=Task.pop(Remove_Task-1)
                print(f"Removed task {Removed_item} successfully!")
            else:
                print("Task not found.")
    elif choice==4:
        print("Exit")
        break
    else:
        print("Please enter a valid choice!")

