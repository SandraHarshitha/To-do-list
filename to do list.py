todo_list=[]
def show_menu():
    print("\n To-Do list options:")
    print("1.View tasks")
    print("2.add task")
    print("3.remove task")
    print("4.exist")
def view_tasks():
    if not todo_list:
        print("no tasks yet!")
    else:
        print("\nyour tasks:")
        for idx,task in enumerate(todo_list,start=1):
            print(f"{idx}.{task}")
def add_task():
    task=input("enter the task:")
    todo_list.append(task)
    print("task added!")
def remove_task():
    view_tasks()
    try:
        index=int(input("enter task number to remove:"))-1
        removed=todo_list.pop(index)
        print(f"removed:{removed}")
    except (ValueError,IndexError):
        print("invalid task number.")
while True:
    show_menu()
    choice=input('choose an option(1-4):')
    if choice=='1':
        view_tasks()
    elif choice=='2':
        add_task()
    elif choice=="3":
        remove_task()
    elif choice=="4":
        print("goodbye!")
        break
    else:
        print("invalid option.please choose 1-4.")



