import socket
import time
IP = "192.168.1.116"
PORT = 4455
ADDR= (IP,PORT)
FORMAT= "utf-8"
SIZE=2048


def main():
	
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect(ADDR)
	file = open("D:/ATM/practica/python/data/test2.cpp", "r")
	data=file.read()
	"""
	client.send("test2.cpp".encode(FORMAT))
	msg = client.recv(SIZE).decode(FORMAT)
	print(f"[SERVER]: {msg}")
	"""

	client.send(data.encode(FORMAT))
	msg = client.recv(SIZE).decode(FORMAT)
	print(f"[SERVER]: {msg}")
    

	msg1 = client.recv(SIZE).decode(FORMAT)
	print(f"[SERVER]:\n{msg1}")

	file.close()
	client.close()	

if __name__ == "__main__":
    main()