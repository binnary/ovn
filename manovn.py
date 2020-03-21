#!/usr/bin/env python3
import socket
import threading
HOST='192.168.6.1'
PORT=1198

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
def action(arg):
    print('read.....')
    while True:
        data=s.recv(1024)
        print(data.decode(),end='')
t = threading.Thread(target=action, args=(1,))
t.start()
while True:
       cmd=input("Please input cmd:")
       cmd += "\r\n"
       s.sendall(cmd.encode())
s.close()
