import sys
import subprocess

def ip_reachability(list):      #define a function to determine if the ip addresses in the list are reachable(turned on and connected)
    for ip in list:             #for every ip address in the list
        ip = ip.rstrip("\n")    #strip the ip address of newline characters

        #variable to store to ping response in a friendlier format
        ping_reply = subprocess.call('ping %s /n 2' %(ip),
                                      #^command to ping ip addr twice
        stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)  #store any output or errors in these variables
        if ping_reply == 0:         #if the ping reply is even(it should be 2)
            print((ip) + " Device is reachable")    #print device is active message
            continue
        else:                   #if the ping response is not even(or there isn't one)
            print("Device is not reachable")    #print device inactive message
