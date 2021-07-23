import datetime
import sqlite3
from sqlite3.dbapi2 import Cursor
from tabulate import tabulate

def cursor():
    return sqlite3.connect('ToDo.db').cursor()

c=cursor()
c.execute('CREATE TABLE IF NOT EXISTS tasks (task_name TEXT,date TEXT)')
c.close()

def add_task():
    c=cursor()
    print("Enter the name of the task to be scheduled in your to do list:")
    task=input()
    today = datetime.date.today()
    with c.connection:
        c.execute("INSERT INTO tasks VALUES(?,?)",(task,today))
    print("Task",c.lastrowid,"has been added to the To Do list :).....")
    c.close()

def display_task():
    c=cursor()
    with c.connection:
        c.execute('SELECT rowid,task_name,date FROM tasks')
    data=[]
    data.append(('TASK NO','TASK NAME','DATE ADDED'))
    data.extend(c.fetchall())
    print(tabulate(data,tablefmt="fancy_grid"))
    c.close()

def delete_task():
    print("Enter the Task that you want to delete from the following tasks....")
    display_task()
    taskno=input("Enter the task no to delete a particular task:")
    c=cursor()
    sql='DELETE FROM tasks WHERE rowid="'+taskno+'"'
    with c.connection:
        c.execute(sql)
    print("The task has been deleted successfully....")
    c.close()