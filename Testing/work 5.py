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

"""
class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')


some_man = Who('John Doe', 42)
print(json.dumps(some_man, default=encode_who))
print(some_man.__class__.__name__)



import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self, z)


class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Who(**d)


some_man = Who('Jane Doe', 23)
json_str = json.dumps(some_man, cls=MyEncoder)
new_man = json.loads(json_str, cls=MyDecoder)

print(type(new_man))
print(new_man.__dict__)



print("g")

class hi():
    def __init__(self, bruh):
        pass

x = hi(76)
print(type(x))

"""







import xml.etree.ElementTree

cars_for_sale = xml.etree.ElementTree.parse('cars.xml').getroot()
print(cars_for_sale.tag)
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    for prop in car:
        print('\t\t', prop.tag, end='')
        if prop.tag == 'price':
            print(prop.attrib, end='')
            print(' =', prop.text)
        else:
            print(' =', prop.text)
        
