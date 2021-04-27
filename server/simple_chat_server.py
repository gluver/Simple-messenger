# -*- coding: utf-8 -*-
"""simple_messager_server
"""

import socket
from threading import Thread

HOST="0.0.0.0"
PORT=8080
HEADER=64
s=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
s.bind((HOST,PORT))
client={}
addresses={}

def handle_client_in(conn,addr):
  name_len=int(conn.recv(HEADER).decode('utf8'))
  nickname=conn.recv(name_len).decode('utf8')
  print(client)
  print(f"{nickname} joined in room")
  broadcast(f"{nickname} joined in room")
  client[conn]=nickname
  while True:
    msg_len=conn.recv(HEADER).decode('utf8')
    if msg_len:
      msg=conn.recv(int(msg_len)).decode('utf8')
      print(f"{nickname}:{msg}")
      broadcast(f"{nickname}:{msg}")
      if msg == "!EXIT": 	 
        del client[conn] 
        print(f"{nickname} left room")
        broadcast(f"{nickname} left room")
        conn.close()
        print(client)
        break 

def broadcast(msg,client=client):
    for conn in client.keys():
      conn.send(f"{msg}".encode('utf8'))


s.listen()
print(f"server launched, listening on port {PORT}")

while True: 
    conn,address=s.accept()
    print(address,"Connected")
    print(conn)
    conn.send("Welcome to the chatting room, please in put your nickname:".encode('utf8'))
    addresses[conn]=address
    Thread(target=handle_client_in,args=(conn,address)).start()
