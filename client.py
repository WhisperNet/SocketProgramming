import socket
import ipaddress

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG ='!dis'
Terminate = 'running'
Welcome = True

def is_valid_local_ip(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)
        return ip.is_private

    except ValueError:
        return False


while Welcome:
    SERVER = input("\nEnter the IP address of the SERVER: ")
    if is_valid_local_ip(SERVER):
        print(f"Client is trying to connect with the server {SERVER}.....")
        break
    else:
        print(f"{SERVER} is not a valid IP address.")

ADDR = (SERVER,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    client.connect(ADDR)
    print("Connection Established\nTo disconnect from the server prompt with !dis")
except:
    print("The given IP has refused to connect. Please check if the server.py is running")
    Terminate = False

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length =str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print("Server Reply: "+client.recv(2048).decode(FORMAT))


while Terminate:
    INPUT = input("Enter Your Message For the SERVER: ")
    print("Wating for the server to reply....")
    send(INPUT)
    if INPUT=='!dis':
        break
