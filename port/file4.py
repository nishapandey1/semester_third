import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip=input("enter your ip address: ")
port=int(input("enter the port you want too scan: "))

port_list=list(port.split(','))

for port in range(port_list):
    result=s.connect_ex((ip,port_list))
if result==0:
    print("port {} is open".format(port))
else:
    print("port{} is close" .format(port))
