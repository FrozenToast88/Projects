# importing datetime allowed me to call certain functions as datetime.now().date()
from datetime import datetime
# Registers the username and password in user.txt
# empty lists 
# open user text document read and write functions applicable
# gear while True allows loop to continue until False
# check while True allows the code to loop through login in user input request until results are obtained
# read lines of user text document
# for loop in lines variable which cont tains user.txt read lines
# each time line loops in through lines it strips replaces synax and splits via a specific syntax
# each data effected by remove variable loops through lines variable and appends a specific character shown by index 
# which will be placed into the empy lists at the begining 

check = True

usern = []
passw = []
print("Welcome to task_manager")
print("Login Information : \n")
register = open("user.txt", "r+")
lines = register.readlines()

for line in lines:
    remove = line.strip().replace(" ", "").split(",")
    usern.append(remove[0])
    passw.append(remove[1])
userName = input("Enter Username : ")
passWord = input("Enter Password : ")
while check:
# as per review changed 'and' to 'or' 
    if userName not in usern or passWord not in passw:
        print("Invalid user information..try again! ")
        print("Login Information : \n")
        userName = input("Enter Username : ")
        passWord = input("Enter Password : ")
    else:
        check = False

# contains requirements of task 2
# Initail if statement which goes through lists to check who is loging in
# f string allowing us to call varaibles as we please

# as per review when logining in as admin options would not run so i placed everything to do with the option in the while loop that holds admin
while check == False:
    if userName in usern and passWord in passw and userName == "admin":
        print(f"Welcome {userName}\n")
# requested input which contains the options which admin will only see.
# task 2 request
        option = input("Please select one of the following options : \nr - register user \na - add task \nva - view all tasks \nvm - view my task \nds - display statistics \ne - exit \nEnter your option here :")

    elif userName in usern and passWord in passw:
            print(f"Welcome {userName}\n")
    
            option = input("Please select one of the following options : \nr - register user \na - add task \nva - view all tasks \nvm - view my task \ne - exit \nEnter your option here :")

# this if statement contains the variable option which contains data that we need to allow the code to run accourding to the data.
# requested input to reregister user data.
# if requirements are met the data will be appended to the the lists containing the registery data
# write the new user data into user.txt 
    if option == "r" or option == "R":
        if userName == "admin":
            new_usern = input("Enter new username : ")
            new_passw = input("Enter new password : ")
            con_passw = input("Confirm new password : ")
            print(f"The user {new_usern} {con_passw} has bean capture")
# "personal while statement" if varaible con_passw and new_passw dont match it will prompt the came input varaible until requirements are met
            while con_passw != new_passw:
                print("New password and confirm new password does not match!")
                con_passw = input("Confirm new password : ")
# due to previous review corrected the indentation needed 
            if new_passw == con_passw:
                usern.append(new_usern)
                passw.append(con_passw)
                login_newDetails = ("\n" + str(new_usern) + ", " + str(con_passw))
                register.write(login_newDetails)
        else:
            print("This option is not accessable to you at this moment in time. ")




# this if statement contains data requested from option variable required for the rest of the code to run.
# open tasks text document because data needs to be writen in it
# username input requested
# all user inputs for the task which needs to be captured takes place via task.write which is captured onto the task.txt document
# close task_info text document
    if option == "a" or option == "A":  
        task_info = open("tasks.txt", "a+")
        task_userName = input("Enter task username : ")
        task_title = input("Enter the title of your task : ")
        task_descr = input("Enter task description : ")
# I obtained this function through research on a website
# this allows me to obtain current date
# website:URL:https://speedysense.com/get-current-date-time-python
        current_date = datetime.now().date()
        task_assDate = current_date
        task_dueDate = input("Enter due date exp: yyyy/mm/dd :  ")
        task_completed = ("No")

# as requested by previous review 
        task_info.write("\n" +task_userName+ ", " +task_title+ ", " +task_descr+ ", " +str(current_date)+ ", " +task_dueDate+ ", " +task_completed)
        task_info.close()




# this if statement run code when requirements are met "va" raviation
# this for statement loops through data in task_info allow us to call specific data
# remove2 changes the data read from task.txt into a list format to be able to manage and call data more efficiently
# this print statement contains concatenated data of specific data by using index thats called from tasks text document for all users
    if option == "va" or option == "Va" or option == "vA" or option == "VA":
        task_info = open("tasks.txt", "r")
        taskLine = task_info.readlines()
        for line in taskLine:
            remove2 = line.strip().split(", ")
            print("Task :               "+ str(remove2[1]))
            print("Assigned to :        "+ str(remove2[0]))
            print("Date assigned :      "+ str(remove2[3]))
            print("Date due :           "+ str(remove2[4]))
            print("Task Complete? :     "+ str(remove2[5]))
            print("Task description :\n "+ str(remove2[2]))




# this if statement run code when requirements are met "vm" raviation
# this for statement loops through data in task_info allow us to call specific data
# this print statement contains concatenated data of specific data by using index thats called from tasks text document for only logged in user
# close task_info document
    if option == "vm" or option == "Vm" or option == "vM" or option == "VM":
        task_info = open("tasks.txt", "r")
        read = task_info.readlines()
        for line in read:
            temp = line.strip().split(",")
            if temp[0] == userName:          
                print("Task :               "+ str(temp[1]))
                print("Assigned to :        "+ str(temp[0]))
                print("Date assigned :      "+ str(temp[3]))
                print("Date due :           "+ str(temp[4]))
                print("Task Complete? :     "+ str(temp[5]))
                print("Task description :\n "+ str(temp[2]))
                task_info.close()
    



        
# this if statement run code when requirements are met "va" raviation and is exclusive to the user "admin"
# this print statement contains a concatanated data and specific data from the list in the begining in numerical form
# open tast.txt to call data so that we read and manipulate them
# we needed a interge variable to be called in the for loop
# this for loop runs through each line and adds a 1 to line allowing us to get the total amount of tasks
    if option == "ds" or option == "Ds" or option == "dS" or option == "DS" and userName == "admin":
        print("Total number of users : " + str(len(usern)))
        task_info = open("tasks.txt", "r")
        taskLine = task_info.readlines()
        line = 0
        for line in range(len(taskLine)):
            line += 1
        print("Totla number of Tasks : "+ str(line))




# this if statement when requirments are met it will exit the user out of the program
# obtained the knowledge of exit() from lecturor
# gear turns false when option 'e' is prompt
    if option == "e" or option == "E":
    
        exit()
    register.close()

else:
    print("Invalid user information ")
