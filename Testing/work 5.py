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


