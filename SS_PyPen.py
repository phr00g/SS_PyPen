import socket
import requests

#takes inputed website and adds 'https://' before it for python requests lib
def fix_name(given):
    fixer = "https://" + given
    return fixer

#gets http response header from response object
def get_head(respo):
    temp = str(respo)
    g = int(temp[11:14])
    return g

## implement socket port scanner

def port_scanner(target):
    print("Starting port scan on " , target)
    for port in range(1,440):
        g = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = g.connect_ex((target,port))
        if result == 0:
            print("Port "  , port , " is open")
        g.close()
        





#subdirectory bust function
def robot_check(fixed_name):
    check_list = ["/robots.txt" , "/sitemap.xml" , "/admin" , "/wp-admin" , "/cpanel" ]

    for directory in check_list:
        more_fixed = fixed_name + directory
        respy = requests.get(more_fixed)
        head = get_head(respy)
        print("Checking for " , more_fixed , "\n\n")
        if (head == 200):
            print("It was found, and is accessible at: " , more_fixed,"\n\n")
        else:
            print(more_fixed, " was not accessible\n")

def main():
    #creates socket object for all socket actions
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)



    targ = input("Please enter the target's host name, ex: www.google.com :\n")

#resolves ip from dns name
    ip = socket.gethostbyname(targ) 

#fixes  name for socket usage
    fixed_name = fix_name(targ)



    print("The host is up, and its public IP address is: " , ip)

    #http get request from target
    response = requests.get(fixed_name)


    #extracts header from http request
    resp_header = get_head(response)

    
    print("The HTTP header is " , resp_header , " ")

    #invokes subdirectory busting function on target
    #robot_check(fixed_name)

    port_scanner(ip)

    
  
                  

    


main()






