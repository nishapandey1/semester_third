import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip=input("Please enter the IP you want to scan: ")
ports=input("Please enter the ports you want to scan (use '-' to give range): ")

# 70-80
port1,port2=(ports.split('-'))
port1=int(port1)
port2=int(port2)

for port in range (port1,port2+1,1):
    result=s.connect_ex((ip,port))

    if(result==0):
        print("Port {} is open".format(port))
    else:
        print("Port {} is closed".format(port))


