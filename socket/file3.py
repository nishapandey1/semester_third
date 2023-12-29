import socket
import sys 
try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket sucessfully created with Address Family IPV4")
except socket.error as err:
    print("socket ceation failed with error message:%s" %(err))
port=80
try:
    host=socket.gethostbyname('www.google.com')
except socket.gaierror:
    print("error reesolving the host")
    sys.exit()
s.connect((host,port))
print("socket successfully connectd to website")
