import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip=input("enter your ip address ")
port1=int(input("enter port1 "))
port2=int(input("enter port2 "))

for port in range(port1,port2):
    result=s.connect_ex((ip,port))
    if(result==0):
        print("port {} is open".format(port))
    else:
        print("port {} is close". format(port))
