''' 1. scanning the single port only
2. scanning range of ports
3.scanning selected ports
4. scanning
    system or well-known ports: from 0 to 1023
    user of registered ports: from 1024 to 49151
    Dynamic or private ports: 49152 to 65535
5. Scanning all ports
6.exit'''
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=input("enter ip address: ")
def singleport():
    
    port=int(input("enter the port you want to scan: "))
    result=s.connect_ex((ip,port))
    if (result ==0):
        print("port {} is open" .format(port))
    else:
        print("port {} is close" .format(port))


def rangeport():
  
    port1=int(input("enter port1 "))
    port2=int(input("enter port2 "))

    for port in range(port1,port2):
        result=s.connect_ex((ip,port))
        if(result==0):
            print("port {} is open".format(port))
        else:
             print("port {} is close". format(port))

def selectedport():
   
    port=input("Please enter the ports you want to scan using ',': ")
    
    port_list=list(port.split(','))

    for i in port_list:
        port=int(i)
        result=s.connect_ex((ip,port))

        if(result==0):
            print("Port {} is open".format(port))

        else:
            print("Port {} is close".format(port))


def scan():

    print("choose an options:")
    print("\n1. system or well-known ports: from 0 to 1023 ")    
    print("\n2. user of registered ports: from 1024 to 49151")    
    print("\n3. Dynamic or private ports: 49152 to 65535")    
    user_choice=int(input("enter your options:"))  

    match user_choice:
        case 1:
            for port in range(0,1023+1,1):
                result=s.connect_ex((ip,port))
                if(result==0):
                    print("port {} is open". format(port))
                else:
                    print("port {} is closed". format(port))

        case 2:
            for port in range(1024,49151+1,1):
                result=s.connect_ex(ip,port)
                if(result==0):
                    print("port{} is open". format(port))
                else:
                    print("port{} is closed". format(port))

        case 3:
            for port in range(49152,65535+1,1):
                result=s.connect_ex(ip,port)
                if(result==0):
                    print("port {} is open". format(port))
                else:
                    print("port {} is closed". format(port))

    
def allport():

    for port in range (0,65535):
        result=s.connect_ex(ip,port)
        if(result==0):
            print("port {} is open". format(port))
        else:
            print("port {} is closed". format(port))

def conti():
    a=int(input("You wanna continue: \n1.yes \n2. no \n"))
    match (a):
        case 1:
            scan_port()
        case 2:
            exit()

def scan_port():
    print("enter your choice:")
    print("\n1.scanning the single port only")
    print("\n2.scanning range of ports")
    print("\n3.scanning selected ports")
    print("\n4.Scanning ports")
    print("\n5.scan all the port")
    print("\n6.exit")

    n=int(input("Choose your option: "))
    match(n):
        case 1:
            singleport()
            conti()
        case 2:
            rangeport()
            conti()
        case 3:
            selectedport()
            conti()
        case 4:
            scan()
            conti()
        case 5:
            allport()
            conti()
        case 6:
            exit()
         
scan_port()