import signal
import socket
import subprocess
import os

bash_script = "/home/dragos/Docker/D1/script.sh"
IP = "192.168.1.116"
PORT = 5000
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 2048


def write_now(filep, msg):
    filep.write(msg)
    filep.flush()
    os.fsync(filep)

def main():
    print("[STARTING] Server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] Server is listening.")

    log = open("/home/dragos/Docker/D1/logger.log", "a")

    while True:

        conn, addr = server.accept()
        write_now(log,f"[NEW CONNECTION] {addr} connected.\n\n    SOURCE\n")
        
        file = open("/home/dragos/Docker/Storage/this.cpp", "w")

        data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] File data received.")
        write_now(file,data)
        write_now(log,data)

        file.close()

        subprocess.call(['bash','/home/dragos/Docker/D1/script.sh'])

        with open('/home/dragos/Docker/error.txt', 'r') as f:
            data2 = f.read()
        f.close()

        conn.send(data2.encode(FORMAT))
            
        file1 = open("/home/dragos/Docker/rezult.txt", "r")
        data1 = file1.read()
        write_now(log,"\n\n    RESULT\n" + data1 + "\n\n")
        conn.send(data1.encode(FORMAT))

        file1.close()

        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")
    

if __name__ == "__main__":
    main()