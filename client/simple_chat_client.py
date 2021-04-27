# -*- coding: utf-8 -*-
"""Simple_messenger_client
"""

import socket
from threading import Thread

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST="172.17.0.2"
PORT=8080
HEADER=64
s.connect((HOST,PORT))                          
def recv_msg(s=s):
  while True:
    try:
      msg=s.recv(1024).decode('utf8')
      print(msg)
    except:
      break
def send_msg(s=s):
  while True:
    msg=input()
    if msg=='!EXIT': break
    msg_len=str(len(msg)).encode('utf8')
    msg_len_padded=msg_len+b' '*(HEADER-len(msg_len))
    s.send(msg_len_padded)
    s.send(msg.encode('utf8'))
    print('\033[1A\033[K')

recv_msg_thread=Thread(target=recv_msg)
recv_msg_thread.start()

send_msg_thread=Thread(target=send_msg)
send_msg_thread.start()
