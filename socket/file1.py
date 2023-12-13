import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# ip='142.250.193.132'
# port=80
# print(ip)
# s.connect((ip,80))
# print("Connection Successfully!")

ip=socket.gethostbyname("www.google.com")
print(ip)
port=80
s.connect((ip,port))
print("connection successfuly")
