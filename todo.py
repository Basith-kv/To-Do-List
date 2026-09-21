import json

def save_task():
    with open ("tasks.json","w") as file:
        json.dump(tasks,file)

def load_tasks():
    try:
        with open("tasks.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

def add_task():
    task=input("Enter The Task:")
    task_data={"task": task,
               "completed":False
               }
    tasks.append(task_data)
    save_task()
    print("Task Added Successfully")

def view_task():
    if len(tasks)==0:
        print("No Tasks Available")
    else:
        print("\nYour Tasks:")
        for i,item in enumerate(tasks,start=1):
            if item["completed"]:
                status="Completed"
            else:
                status="Pending"
            print(i,item["task"],"-",status)

def Complete_task():
    view_task()
    try:
        Number=int(input("Enter Task Number To Complete:"))
        if 1<=Number <=len(tasks):
            tasks[Number-1]["completed"]=True
            save_task()
            print("Task Completed")
        else:
            ("invalid Task Number!")
    except ValueError:
        print("Please Enter a Number:")

def Delete_Task():
    view_task()
    
    try:
        Number=int(input("Enter The Delete Task Number:"))
        if 1<=Number <=len(tasks):
            tasks.pop(Number-1)
            save_task()
            print("Task Deleted")
        else:
            print("invalid Task Number")
    except ValueError:
        print("Please Enter a Number")

def pending_tasks():
    print("\nPending Tasks:")

    for i,item in enumerate(tasks,start=1):
        if item["completed"]==False:
            print(i,item["task"])

def completed_tasks():
    print("\nCompleted Tasks:")

    for i,item in enumerate(tasks,start=1):
        if item["completed"]==True:
            print(i,item["task"])

tasks=load_tasks()

while True:
    print("\n---TO DO LIST---")
    print("1.Add Task")
    print("2.View Task")
    print("3.Complete Task")
    print("4.Delete Task")
    print("5.Pending Tasks")
    print("6.Completed Tasks")
    print("7.Exit")

    Choice=input("Enter Your Choice:")

    if Choice == "1":
        add_task()
    elif Choice == "2":
        view_task()
    elif Choice == "3":
        Complete_task()
    elif Choice == "4":
        Delete_Task()
    elif Choice == "5":
        pending_tasks()
    elif Choice == "6":
        completed_tasks()
    elif Choice == "7":
        print("Thanku")
        break
    else:
        print("invalid Option")



