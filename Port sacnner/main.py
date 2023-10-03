#scanning for the open ports
from queue import Queue
import socket
import threading

queue = Queue()

#ip adddress of the target
target = '192.168.1.1'
open_port = []

def portscann(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return False


# #scanning the list of port
# for port in range(1,255):
#     result = portscann(port)
#     if result:
#         print("Port connected")
#     else:
#         print("Port close")


def fill_queue(port_list):
    for port in port_list:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if portscann(port):
            print("{} is open".format(port))
            open_port.append(port)


port_list = range (1,1024)
fill_queue(port_list)

thred_list = []

#creating the threads sets with number of 10 ports
for thr in range(10):
    thread = threading.Thread(target=worker())
    thred_list.append(thread)


for thread in thred_list:
    thread.start()


for thread in thred_list:
    thread.join()


print("open ports : " , open_port)


