import ToDo
choice=input("This program requires tabulate module to work. If you havent installed it then try running \"pip install tabulate\" on the command line. Continue? [yes/no]")
if str.lower(choice)=="no":
    exit()
print("=================TO DO LIST=================")
print("1. Schedule a new task to your To Do list")
print("2. Display all your tasks")
print("3. Delete a task")
choice=int(input("Enter your choice:"))
if choice==1:
    print(ToDo.add_task())
elif choice==2:
    ToDo.display_task()
elif choice==3:
    ToDo.delete_task()
else:
    print("Wrong choice Entered")