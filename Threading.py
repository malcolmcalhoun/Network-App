import threading
#function to create threads
def create_threads(list, function):
    threads = []        #list to store threads
    for ip in list:     # for every ip address in the list
                        # create a variable to store each thread
        th = threading.Thread(target = function, args = (ip,)) # args is a tuple with a single element
        th.start()      #initialize threads
        threads.append(th) #add each thread to the threads list

    for th in threads:      #for loop to join threads together
        th.join()
