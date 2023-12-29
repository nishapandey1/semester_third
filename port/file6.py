import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(1)
ip=input("Please enter the IP you want to scan: ")

for port in range (0,65535+1,1):
    result=s.connect_ex((ip,port))
    if(result==0):
        print("port {} is open". format(port))
    else:
        print("port {} is closed". format(port))