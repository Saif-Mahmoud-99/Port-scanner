import socket # this mosdule used in port scanner that open connection with the victim machine

import sys # this module used to store arguments in sys.argv

from datetime import datetime # this module used to get the current time or use anything specialize time

import pyfiglet # this module used to print the name of tool on screen 

#----------------------------------------------------------------------------------------------------------------------

ascii_banner = pyfiglet.figlet_format("Caeser Scanner") # this line convert the name as ascii form 
print(ascii_banner)

if len(sys.argv) == 2: # her check if the total number of argument equal 2 excute the function of if statement and must be 2 argument 
    target = socket.gethostbyname(sys.argv[1]) # we will use socket to get The name of the host system for which IP address resolution is needed by using argument[1].

else:
    print("Invalid amount of arguments you must enter the IP address !") # if you dont enter the argument this message will be the output

print("-" * 50) # to print this form --------------------------------------
print("Scanning Target: " + target) # to print the target ip
print("Scanning started at: " + str(datetime.now())) # to print the current time of program running
print("-" * 50) # to print this form --------------------------------------

try:
    for port in range(1,1000):
    
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET --> IPv4 , SOCK_STREAM --> TCP
        socket.setdefaulttimeout(5) # time of scanning for each port
        result = s.connect_ex((target,port)) # her the arguments ip address, port number. connect_ex doing if port is opened the return will be 0 if the port is closed will return any number else

        if result == 0: # the result refer to the port is opened or closed 0 --> mean open
            print("port {} is open".format(port)) # print message that port is opened
        s.close() # end scanning for single port 

except KeyboardInterrupt:
    print("\n Exiting Program !!!!")
    sys.exit()

except socket.gaierror:
    print("\n Hostname couldn't be resolved !!!!")
    sys.exit()

except socket.error:
    print("\n Server not responding !!!!")
    sys.exit()
