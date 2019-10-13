# TO DO APP- DICT

print(""" Todo_app """)

tasklist = []  # we need each task to be an instance with
# various features here.
# name
# duedate
# status
# priority


tasks = {'do_homeworks': {'key_name': 'dohomeworks',
                          'key_duedate': '13october',
                          'key_status': 'completed',
                          'keypriority': 'very_imp'}}
incompleted_tasks = []
for key,val in tasks.items():
    if key['key_status'] == 'incompleted':
        incompleted_tasks.append(i)


# my_dict = {'hacker': True, 'age': 72, 'name': 'John Doe'}
# for val,key in my_dict.items():
#     print(val)
#

def add_task():
    constant = 10000
    while a > 0:
        key_name = input("Enter the task name you would like to add: ")
        key_duedate = input("and the tasks duedate: ")
        key_status = input("is it completed or incomplete: ")
        key_priority = input("""is it a priority task,
                             name it as 'important'
                             or 'not important' """)

        tasks[key_name]['key_name'] = key_name
        tasks[key_name]['key_duedate'] = key_duedate
        tasks[key_name]['key_status'] = key_status
        tasks[key_name]['key_priority'] = key_priority

def delete_task():
    to_be_deleted = input("Enter the name of the task to be deleted: ")
    tasks.pop(to_be_deleted)
    print(to_be_deleted, "has been succesfully deleted.")

def set_due_date():  # to  a task
    to_be_duedated = input("Enter the value you wanna add due date to: ")
    key_duedate = input("Enter the duedate: ")
    tasks[to_be_duedated]['key_duedate'] = key_duedate
    print("a")#burada key value ciftini yazidr

def show_status():
    to_show_status = input("Enter the name of the task you wanna check status: ")
    print(tasks[to_show_status]['key_status'])
    if tasks[to_show_status]['key_status'] == "incomplete":
        print(incompleted_tasks)
    # if incompleted display incompleted task list

def complete_task():
    to_be_completed = input("Enter the task name to be completed: ")
    tasks[to_be_completed]['key_status'] = 'completed'

def set_priority():
    to_setprio = input("Enter the task name to add priority: ")
    prio_tobe_setted = input("Enter the priority of the task: ")
    tasks[to_setprio]['key_status'] = prio_tobe_setted


a = 1000
while a > 0:
    userinp = input("""Welcome to TODO LIST!!!
Press 1 to add a task,
      2 to delete a task,
      3 to set a due date to an existing task,
      4 to show the status of a task()if it is completed/incomplete,
      5 to complete a task,
      6 to set priority to a task.""")
    if userinp == 1:
        add_task()
    elif userinp == 2:
        delete_task()
    elif userinp == 3:
        set_due_date()
    elif userinp == 4:
        show_status()
    elif userinp == 5:
        complete_task()
    elif userinp == 6:
        set_priority()
