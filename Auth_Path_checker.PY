import paramiko
import os.path
import time
import sys
import re

user_file = input("Enter User_File Path Name") #get input from user
if os.path.isfile(user_file) == True: #Check if the file exists using os.path
    print("File Path is Valid")     #if it exists print this
else:
    print("File does not exist")    #if it doesn't print this
cmd_file = input("Enter Cmd File Path Name") #get input from user
if os.path.isfile(cmd_file) == True: #Check if the file exists using os.path
    print("File Path is Valid")     #if it exists print this
else:
    print("file does not exist")  #if it doesn't print this
    sys.exit()                  #close sys connection

def ssh_connection(ip):  #Function to use SSH to connect to a device using it's IP
    global user_file
    global cmd_file

    try:
        selected_user_file = open(user_file, 'r')       #open user file and read
        selected_user_file.seek(0)                      #start from the beginning of the file

        #username is the first item on the first line of the user file stripped of newline characters
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")

        selected_user_file.seek(0)                      #go back to the beginning of the user file

        #the password is the second item on the first line of the userfile stripped of newline characters
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")

        session = paramiko.SSHClient()      #assign the paramiko library SSHclient function call to a variable
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())#THIS IS A SECURITY RISK IN A DEVELOPMENT ENVIRONMENT REPLACE paramiko.AutoAddPolicy W/ HOST KEYS
        session.connect(ip.rstrip("\n"), username = username, password = password)  #connect to the ip addres given and use the username and password given to log in
        connection = session.invoke_shell()     #assign the invoke_shell function call on the paramiko session to a variable(open a coammnd line shell)

        connection.send("enable\n") #send enable command to the shell
        connection.send("terminal length 0\n")  #send the terminal length command to the shell
        time.sleep(1) #pause

        connection.send("\n")   #send spacebar command
        connection.send("conf t\n") #send the configure terminal command to shell
        time.sleep(1)   #pause

        selected_cmd_file = open(cmd_file, 'r') #open command file and read
        for each_line in selected_cmd_file.readlines(): #for each line in the command file
            connection.send(each_line + "\n") #send each line as a command to the terminal
            time.sleep(2) #pause for 2 seconds

        selected_user_file.close()  #close connection to user File
        selected_cmd_file.close()   #close connection to command file

        router_output = connection.recv(65535)  #assign the router output to a variable and fill it with as much iformation as possible
        if re.search(b"% Invalid input", router_output): #search the router output for any invalid input commands
            print("Error on Device " + (ip))    #if there are any invalid input commands print Error message
        else:
            print("Finished Device " + (ip))     #else print finished message
            #print(str(router_output) + "\n")        #print the router output


        cpu =  re.search(b"%Cpu\(s\):(\s)+(.+?)(\s)+us," , router_output)
        utilization = cpu.group(2).decode("utf-8")
        with open("C:\\Users\\Malcolm\\PythonNetApp\\Reading and writing files via SSH\\cpu.txt", "a") as f:
            f.write(utilization + "\n")
        session.close()         #close the SSHclient session

    except paramiko.AuthenticationException:        #exception in case an invalid username or password is entered at the start of the program
        print("Invalid Username or Password. Check Device Configuration")
        print("Exiting program")
