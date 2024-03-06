import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG ='!dis'
#################################################
# Assign the local IP address of the SERVER to the SERVER variable
SERVER = socket.gethostbyname(socket.gethostname())
#SERVER = ''
#################################################
ADDR = (SERVER,PORT)
Terminate = 'running'
Welcome = True
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length =str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print("Server Reply: "+client.recv(2048).decode(FORMAT))

if Welcome:
    print("     Client is trying to connect with the server.....")
    print("     Connection Established\n     To disconnect from the server prompt with !dis")

while Terminate:
    INPUT = input("Enter Your Message For the SERVER: ")
    print("Wating for the server to reply....")
    send(INPUT)
    if INPUT=='!dis':
        break
