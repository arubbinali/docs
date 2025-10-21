import socket
"""
try:
        
    server_addr = input("What server do you want to connect to? ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_addr, 80))
    sock.send(b"GET / HTTP/1.1\r\nHost: " +
            bytes(server_addr, "utf8") +
            b"\r\nConnection: close\r\n\r\n")
    response = sock.recv(10000)
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    print(repr(response))
    print("ay")
except Exception as exception:
    print("nah", f"\nwe got a problem yo:\n{exception}")
"""
"""
server_addr = input("What server do you want to connect to? ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_addr, 11111))
sock.send(b"GET / HTTP/1.1\r\nHost: " +
        bytes(server_addr, "utf8") +
        b"\r\nConnection: close\r\n\r\n")
response = sock.recv(10000)
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(repr(response))
"""
import json


"""
x = 234
y = json.dumps(x)
print(type(y))
print(type(str(x)))

comics = '"The Meaning of Life" by Monty Python\'s Flying Circus'
print(json.dumps(comics))

my_dict = {'me': "Python", 'pi': 3.141592653589, 'data': (1, 2, 4, 8), 'set': None}
print(json.dumps(my_dict))
"""


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


some_man = Who('John Doe', 42)
print(json.dumps(some_man))