import socket
import thread
import sys

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM )

try :
    s.bind(server, port)
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for Connection, Server Started")

def threaded_client(conn):
    pass