# Simple-messenger
## 1.How to build docker image
Clone the repo onto your  machine  
1. Enter `Simple-messenger/server`,in terminal run:  
```shell 
$ docker build -t simple-chat-server .
``` 
 
```shell
Sending build context to Docker daemon  4.096kB
Step 1/4 : FROM python:3.8.9-alpine3.12
3.8.9-alpine3.12: Pulling from library/python
339de151aab4: Already exists 
a860e27ad689: Already exists 
a29b13e18c5f: Already exists 
199eca30397d: Already exists 
9a17247e8d35: Already exists 
Digest: sha256:10d97b97cce729cdf089c24b76662ba3c8f623632abe255bc7efa2a9add52f42
Status: Downloaded newer image for python:3.8.9-alpine3.12
 ---> 37859e229780
Step 2/4 : WORKDIR /
 ---> Running in cd9ee62bd2dc
Removing intermediate container cd9ee62bd2dc
 ---> ba0e6ebff33f
Step 3/4 : COPY . .
 ---> e5ea6b3a6ddf
Step 4/4 : CMD ["python3","simple_chat_server.py"]
 ---> Running in bc3d62371edf
Removing intermediate container bc3d62371edf
 ---> 687cba09e3b2
Successfully built 687cba09e3b2
Successfully tagged simple-chat-server:latest
```
2. Enter Simple-messenger/client,run:  
 ```shell
 $ docker build -t simple-chat-client .
 ```   
  
 ```shell
 Sending build context to Docker daemon  3.584kB
Step 1/4 : FROM python:3.8.9-alpine3.12
 ---> 37859e229780
Step 2/4 : WORKDIR /
 ---> Using cache
 ---> ba0e6ebff33f
Step 3/4 : COPY . .
 ---> 3576e40d469a
Step 4/4 : CMD ["python3","simple_chat_client.py"]
 ---> Running in 99644ccd8d3d
Removing intermediate container 99644ccd8d3d
 ---> c17602966efc
Successfully built c17602966efc
Successfully tagged simple-chat-client:latest
```
## 2.Run server:  
```shell
$ docker run -it simple-chat-server
```
```shell
server launched, listening on port 8080
```
## 3.Run clients:
Run clients in new terminals .For each client in each terminal:  
```shell
$ docker run -it simple-chat-client
```  
Input a nickname then press enter,after that input messages for testing:  
```shell
Welcome to the chatting room, please in put your nickname:
client1
```
Repeat this step for multiple clients
```shell
Welcome to the chatting room, please in put your nickname:
client2
```
```shell
Welcome to the chatting room, please in put your nickname:
client3
```
Input some message for each client 
```shell
Welcome to the chatting room, please in put your nickname:


client1:Hi
client3 joined in room
client3:Hey
Fine
```
```shell
Welcome to the chatting room, please in put your nickname:


client3:Hey
client1:Fine

```
