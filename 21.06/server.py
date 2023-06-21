import socket
import subprocess


bash_script = "/home/dragos/Docker/D1/script.sh"
IP = "192.168.1.116"
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 2048



def main():
    print("[STARTING] Server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] Server is listening.")

    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        """
            filename = conn.recv(SIZE).decode(FORMAT)
            print("[RECV] Filename received.")
            f="/home/dragos/Docker/Storage/"+filename
            conn.send("Filename received.".encode(FORMAT))
        """
        file = open("/home/dragos/Docker/Storage/this.cpp", "w")

        data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] File data received.")
        print(data)
        file.write(data)
        conn.send("File data received.".encode(FORMAT))

        file.close()

        subprocess.call(['bash','/home/dragos/Docker/D1/script.sh'])
        
        file1 = open("/home/dragos/Docker/rezult.txt", "r")
        data1 = file1.read()
        conn.send(data1.encode(FORMAT))

        file1.close()

        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")

if __name__ == "__main__":
    main()