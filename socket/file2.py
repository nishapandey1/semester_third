import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# ip=socket.gethostbyname("www.softwarica.edu.np")
# print(ip)
# port=80
# s.connect((ip,port))
# print("connection successfuly")

# ip= '34.160.17.71'
# port=80
# print(ip)
# s.connect((ip,port))
# print("Connection Successfully!")

'''localhost'''
ip='127.0.0.1'
port=8000
s.connect((ip,port))
print('connection sucessfully!')
