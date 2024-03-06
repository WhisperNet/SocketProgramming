import socket
import threading
HEADER = 64
PORT = 5050
#################################################
# Assign your local IP address to the SERVER variable
SERVER = socket.gethostbyname(socket.gethostname())
#SERVER = ''
#################################################
ADDR = (SERVER, PORT)
FORMAT= 'utf-8'
DISCONNECT_MSG = '!dis'
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn,addr):
    print(f"NEW Connection From {addr}")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
                conn.send("You are disconnected!!!".encode(FORMAT))
                print(f"The [{addr}] client has isuued the disconnect command and has been DISCONNECTED")
            print(f"[{addr}] says: {msg}")
            if msg!= DISCONNECT_MSG:
                conn.send(input("Sent a reply to the client: ").encode(FORMAT))
                print("Wating for client to send a message.....")
    conn.close()


def start():
    server.listen()
    print(f"Listening on {SERVER}\n")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"This Client will be handled by Thread No: {threading.active_count()-1}\nWating for client to send a message.....")


print("STARTING SERVER....")
start()
