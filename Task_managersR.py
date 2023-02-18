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
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        #Ask user to enter the username and password to register.
        #Check if user enter the correct password the second  time and if it doesn't match, return error.
        #If user enters the correct password, write the user name and password on user.txt.
        if user_name == 'admin':
            new_user = input("Enter user name to register: ")
            password = input("Enter new password:  ")
            chk_psw  = input("Confirm your password: ")
            if password ==chk_psw:
                user_file = open('user.txt', 'a')
                user_file.write('\n' + new_user + ', ' + password)
                user_file.close()
            else:
                print("Your password doesn't match: ")
        else:
            print("You don't have authorisation to register.")


    elif menu == 'a':
        pass
        #Open tasks.txt file to append new task.
        #Ask user to enter the user's name to assign task, task title and description and due date.
        # Add assigned date using datetime.today and change format to dd month, year.
        # Create variable(new_assgn) containing all elements to write on task.txt and print it.
        # Write new_assgn on tasks.txt. 

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

    elif menu == 'va':
        pass
        #Open tasks.txt with read and loop through lines using for loop.
        #Split text data with comma to create a list.  
        #Format each element by defining output format.
        #Print each line as per format and close file.
        task_file = open('tasks.txt', 'r')
        data = task_file.readlines()
        for line in data:
            split_data = line.split(", ")

            output = '***************************\n'
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

    elif menu == 'vm':
        pass
        #Open tasks.txt to read tasks of the logged in user.
        #Print logged in user name to check.
        #Read data from tasks.txt using readlines.
        #Create list(user_task) to append task of the logged in user from tasks.txt.
        #Use for loop to go through tasks.txt line and split it to create list.
        #Check if logged in user name is contained in the list and if it is, append it to user_task.
        #Format the logged in user task and print.

        task_file = open('tasks.txt','r')
        my_name = print(user_name)
        my_data = task_file.readlines()
        user_task = []


        for line in my_data:
            split_data =line.split(',')
            if user_name in line:
                user_task.append(line)
                output = '***************************\n'
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

    elif menu == 'ds':
        #Check if the user is 'admin or not. 
        #If user is admin, read data from user.txt to generate statistics. 
        #Number of user is equal to number of line in text file, therefore, use len(line) to get numbers
        #print the number of user and tasks.
        if user_name =='admin':
            user_file = open('user.txt','r')
            num_user = 0
            num_user = len(user_file.readlines())
            print('The number of user is:', num_user)

            user_file.close()
            
            task_file = open('tasks.txt','r')
            num_task = 0
            num_task = len(task_file.readlines())
            print('The number of task is:', num_task)
            
            task_file.close()
        
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")