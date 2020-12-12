import sys
import time 
from IP_list_generator import ip_list_generator
from IP_reachability_checker import ip_reachability
from IP_validity_checker import ip_validity_checker
from Auth_Path_checker import ssh_connection
from Threading import create_threads

ip_list = ip_list_generator()           #assign the ip_list_generator function call to a variable
try:    #try clause to check validity of ip list
    ip_validity_checker(ip_list)      #call the ip_validity_checker function on the ip_list
except KeyboardInterrupt:       #except clause to interrupt the program using the CTRL-C command
    print("Program Aborted. Exiting...")    #print exit message
    sys.exit()      #exit
try:    #try clause to check if ip addresses in the ip list are reachable
    ip_reachability(ip_list)    #call the ip_reachability function on the ip list
except KeyboardInterrupt:   #except clause to interrupt the program using the CTRL-C command
    print("Program Aborted. Exiting...") #print exit message
    sys.exit()  #exit
while True:
    create_threads(ip_list, ssh_connection)    #call the create threads function on the ip list and use the ssh_connection as an argument
    time.sleep(10)
