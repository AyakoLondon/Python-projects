#=====importing libraries===========
#Import datetime library 
from datetime import datetime

#====Login Section====
#Open user.txt to read username and password.
#Write name and password in a seperate list using for loop and strip new line and split by comma.
#Append user name and password in respective list.
#Ask user to enter user name and check whether the name is in user list created.
#Use while not loop to prompt user to enter valid name and return error message if user enters invalid username.
#Define index of password with (position) to match once user enters password to validate.
#While password doesn't match the one in the indexed position, return error message and prompt to enter valid password.
#Once user enters valid password, return greeting message.        
user_file = open('user.txt','r')
username_list = []
pasw_list = []
for line in user_file:
    user, pasw = line.strip('\n').split(", ")
    username_list.append(user)
    pasw_list.append(pasw)
   
user_file.close()
print(username_list, pasw_list)

user_name = input("Enter User Name: ")
while not user_name in username_list:
    print(" Enter valid User Name.")
    user_name = input("Enter User Name: ")
    
post = username_list.index(user_name)
print(post)
password = input("Enter password: ")
while password != pasw_list[post]:
    password = input("Enter valid password.")

print(f"Welcome {user_name}")


while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - Generate Reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        #Ask user to enter the username and password to register using 'register'function.
        #Check if user enter the correct password the second  time and if it doesn't match, return error.
        #If user enters the correct password, check if the username already exists or not using for loop to search line in user.txt.
        #If username already exists, return error message.
        #If username doesn't exist, write the user name and password on user.txt.
        def reg_user():
            username = input("Enter a username: ")
            if username =="admin":
                new_user = input("Enter new user name: ")
                password = input("Enter a password: ")
                chk_psw  = input("Confirm your password: ")
            if password ==chk_psw:
                with open("user.txt", "r+") as f:
                    for line in f:
                        if new_user in line:
                            return "New username already exists. Try another username."
                        if new_user not in line:
                            f.write(f"\n{new_user}, {password}\n")
                    return "New user registered successfully."

            if username != "admin": 
                return "Error: only 'admin' can register new users."

        print(reg_user())

    elif menu == 'a':
        #Open tasks.txt file to append new task.
        #Ask user to enter the user's name to assign task, task title and description and due date.
        # Add assigned date using datetime.today and change format to dd month, year.
        # Create variable(new_assgn) containing all elements to write on task.txt and print it.
        # Write new_assgn on tasks.txt. 
        def add_task():
            user_file = open('tasks.txt', 'a')
            task_user = input("Enter username to assign task: ")
            task_name = input("Enter the title of the task: ")
            desc_task = input("Enter the task description: ")
            due_date  = input("Enter due date for task: ")
            today  = datetime.today()
            date_asgn = today.strftime("%d %b %Y")
            print(date_asgn)
            task_status= input("Enter 'yes' or 'no': ")
            new_assgn = f'\n {task_user},{task_name}, {desc_task},{due_date}, {date_asgn},{task_status} \n'
            print(new_assgn)
            user_file.write(new_assgn)
            user_file.close()
    
        print(add_task())
      

    elif menu == 'va':
        #Open tasks.txt with read and loop through lines using for loop.
        #Split text data with comma to create a list.  
        #Format each element by defining output format.
        #Print each line as per format and close file.
        def view_all():
            task_file = open('tasks.txt', 'r')
            data = task_file.readlines()
            for pos, line in enumerate (data):
                split_data = line.split(", ")

            output = f'***********[{pos+1}]****************\n'
            output += '\n'
            output += f'Assigned to:\t\t {split_data[0]}\n'
            output += f'Task title:\t\t {split_data[1]}\n'
            output += f'Task description: \t {split_data[2]}\n'
            output += f'Assigned date:\t\t{split_data[3]}\n'
            output += f'Due date:\t\t {split_data[4]}\n'
            output += f'Completion: \t\t{split_data[5]}\n'
            output += '\n'
            output += '*********************************\n'
            print(output)
            task_file.close()
        print(view_all())

    elif menu == 'vm':   
        #Open tasks.txt to read tasks of the logged in user.
        #Print logged in user name to check.
        #Read data from tasks.txt using readlines.
        #Create list(user_task) to append task of the logged in user from tasks.txt.
        #Use for loop to go through tasks.txt line and split it to create list.
        #Check if logged in user name is contained in the list and if it is, append it to user_task.
        #Format the logged in user task using enumerate to assign number to tasks.
        #Ask the user which task he wishes to edit and prompt to enter task number.
        #If the user gives 0 or larger than the number of tasks in the task list, return error message.
        #Once the user selects task number, show selection menu, 1) to edit due date or 2) mark task completion.
        #If the user selects to edit due date, split task data and specify due date [-2] in the split data and append it.
        #If the user selets to edit task completion, replace the last element of the task with 'yes'.
        #Open task file with 'write' mode and write the edited data.    

        def view_mine():
            with open('tasks.txt','r') as task_file:
                my_name = print(user_name)
                my_data = task_file.readlines()
                user_task = []
    
            for pos, line in enumerate(my_data):
                split_data =line.split(', ')
                if user_name in line:
                    user_task.append(line)

            output = f'**********[{pos+1}]*****************\n'
            output += '\n'
            output += f'Assigned to:\t\t {split_data[0]}\n'
            output += f'Task title:\t\t {split_data[1]}\n'
            output += f'Task description: \t {split_data[2]}\n'
            output += f'Assigned date:\t\t{split_data[3]}\n'
            output += f'Due date:\t\t {split_data[4]}\n'
            output += f'Completion: \t\t{split_data[5]}\n'
            output += '\n'
            output += '*********************************\n'
            print(output)
               
            while True: 
                task_choice = int(input( "Please select the number of task : "))-1
                if task_choice <0 or task_choice> len(my_data):
                    print("You have selected ivalid number. Try again: ")
                    continue

                edit_data = my_data[task_choice]
                break
            while True:
            
                output  = f'***********[Select an option]*********\n'
                output += '1 - Edit due date  \n'
                output += '2 - Mark as completed \n'
                output += '***************************************\n'
                print(output)            

                choice = int(input('Enter your selection: '))
                if choice <=0 or choice >=3:
                    print('You have entered invalid number. Try again:')
                    continue

                if choice == 1:
                    split_data = edit_data.split(', ')
                    split_data[-2]=input("Enter due date in dd/mon/yyyy format: ")
                    alt_data = ", ".join(split_data)
                    my_data[task_choice] = alt_data
                    task_file = open('tasks.txt', 'w')
                    for line in alt_data:
                        task_file.write(line)


                elif choice== 2:
                    split_data = edit_data.split(', ') 
                    split_data[-1]= "Yes\n"
                    new_data = ", ".join(split_data)
                    my_data[task_choice] = new_data
                    task_file = open('tasks.txt','w')
                    for line in my_data:
                        task_file.write(line)
                    print("You have completed task.")
            
                break
            task_file.close()
        print(view_mine())

    elif menu == 'gr':
        #Open task.txt file and check how many tasks are registered by counting number of lines.
        #Check how many tasks have been completed by checking the last element of the line.
        #Check how many tasks are incomplete and also how many are overdue by comparing its due date with current date using date time.
        #Calculate percentage of incomplete tasks and overdue tasks using round function.
        #Format output in userfriendly manner and write the output in task_overview in append mode. 
        #Open user.txt file and check how many users are registered by counting lines.
        #Split task file and check username and append tasks in unique_user list if the username is not duplicate.
        #Count number of tasks of the user in unique_user list.
        #Check if the task is complete or not by checking last element of the list and increase number by 1.
        #Check if the task is incomplete and if it is overdue by checking its due date and compare it with current date.
        #Calculate the percentage of tasks assigned to a given user using round function.
        #Calculate the percentage of tasks completed and incomplete, incomplete and overdue.
        #Format outpput in userfriendly manner and write the output in user_overview.txt in append mode. 
        #Close user_overview.txt.

        def gen_reports():
            task_file = open('tasks.txt','r')
            task_list = task_file.readlines()
            task_file.close()
            user_file = open('user.txt', 'r')
            user_list = user_file.readlines()
            user_file.close()
            total_tasks = 0
            overdue = 0
            incomp_task = 0
            comp_task = 0
            task_overview = ""
            user_overview = ""
            total_user = 0
            unique_users=[]
            tasks_user = 0

            for line in task_list:
                data_list = line.strip('\n').split(', ')
                total_tasks +=1
                if data_list[-1].lower() == 'yes':
                    comp_task +=1
                elif data_list[-1].lower() =='no':
                    incomp_task +=1
                    due_date = data_list[-2]
                    due_date_obj = datetime.strptime(due_date,"%d %b %Y")
                    current_date = datetime.today()
                    if due_date_obj < current_date:
                        overdue+=1
                        percent_overdue = round(((overdue/total_tasks)*100),2) 
                        percent_incomplete =round(((incomp_task/total_tasks)*100),2)
        
            output = f'***************************\n'
            output += '\n'
            output += task_overview + f'Total number of tasks:\t\t {total_tasks}\n'
            output += task_overview + f'Completed tasks:\t\t {comp_task}\n'
            output += task_overview + f'Incomplete tasks:\t\t {incomp_task}\n'
            output += task_overview + f'Incomplete, overdue tasks:\t{overdue}\n'
            output += task_overview + f'Percenetage of incomplete task\t{percent_incomplete}\n'
            output += task_overview + f'percentage of incomplete,overdue \t{percent_overdue}\n'
            output += '\n'
            output += '*********************************\n'
            print(output)
            with open('task_overview.txt','a') as f:
                f.write(output)


            for line in user_list:
                user_list = line.strip('\n').split(', ')
                total_user+= 1
                print(total_user)

            for line in task_list:
                data_list = line.strip('\n').split(', ')
                user = data_list[0]
            if user not in unique_users:
                unique_users.append(user)
                tasks_user = 0
                tasks_user += 1
            if data_list[-1]=='yes':
                comp_task+=1
            else:
                incomp_task+=1
                due_date = data_list[-2]
                due_date_obj = datetime.strptime(due_date,"%d %b %Y")
                current_date = datetime.today()
                if due_date_obj < current_date:
                    overdue+=1

                percent_tasks =  round((tasks_user/total_tasks)*100,2)
                percent_comp  =  round((comp_task/tasks_user)*100,2)
                percent_incomp = round((incomp_task/tasks_user)*100,2)
                percent_overdue= round((overdue/tasks_user)*100,2)

            output = f'***************************\n'
            output += '\n'
            output += user_overview + f'Total number of users:\t\t {total_user}\n'
            output += user_overview + f'Total number of tasks generated:\t\t{total_tasks}\n'
            output += user_overview + f'Number of tasks assigned to given user:\t\t{tasks_user}\n'
            output += user_overview + f'Percentage of tasks completed by that user:\t\t{percent_comp}\n'
            output += user_overview + f'Percenetage of incomplete task of that user:\t{percent_incomp}\n'
            output += user_overview + f'percentage of incomplete,overdue task: \t\t{percent_overdue}\n'
            output += '\n'
            output += '*********************************\n'
            print(output)
            with open('user_overview.txt','a') as f:
                f.write(output)
        print(gen_reports())
    
    elif menu == 'ds':
        #Check if the user is 'admin or not. 
        #If user is admin, call function of generating_report
        #Print the user_overview and task_overview
        if user_name =='admin':
            my_function = gen_reports()
            print(my_function)
            

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")