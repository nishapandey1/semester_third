import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostbyname('www.google.com')
port=80

result=s.connect_ex((host,port))
if(result==0):
    print("port {} is open". format(port))
else:
    print("port {} is closed". format(port))