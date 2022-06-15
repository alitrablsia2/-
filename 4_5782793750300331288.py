import socket
s = socket.socket()
host = socket.gethostname()
port = 9999
s.connect((host,port))
while True:
    m=s.recv(1024).decode()
    print(m)
    msg=input("enter command ")
    s.send(msg.encode())
    print(s.recv(1024).decode())
