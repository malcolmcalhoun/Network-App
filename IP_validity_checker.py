import sys

def ip_validity_checker(list):          #define a function to check if the ip addresses in the list are valid
        for ip in list:         #for every ip address in the list
            ip = ip.rstrip("\n")    #strip each ip of newline characters
            octet_list = ip.split('.')  #and split them up by '.' into a list of octets

            #if the length of the octet list is equal to four
            #and the first octet in the list is between 1 and 223
            #and if the first octet in the list is not 127 or (169 WHILE the second octet is 254)
            #and the second octet in the list is between 1 and 255
            #and the third octet is between 0 and 255
            #then continue
            if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223)\
            and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or \
            int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255 and \
            0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
                continue    #then continue
            else:   #if any of those conditions aren't met
                print("Invalid IP address in File") #print invalid ip address message
                #sys.exit()              #and exit the program
