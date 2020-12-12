import os.path
import sys          #import modules

#Function to check if the IP address is valid
def ip_list_generator():
    ip_address_file = input("Enter IP address File Path Name") #get input from user
    if os.path.isfile(ip_address_file) == True: #Check if the file exists using os.path
        print("File Path is Valid")     #if it exists print this
    else:
        print("File does not exist")   #if it doesn't exist print this
        sys.exit()

    ip_addresses = open(ip_address_file, 'r')   #open IP address file and read
    ip_addresses.seek(0)    #starting from the beginning of the file
    ip_list = ip_addresses.readlines()  #add all the ip address to a list
    ip_addresses.close()
    return ip_list
