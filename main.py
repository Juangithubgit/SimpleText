import random
import string
import turtle
# import pygame
import time
import math
from simple_make import SimpleMake

global graph
dumbo_list_of_things = {
    'run_if': 'while',
    'show': 'print',
    'do_this': ':',
    'then_do': ':',
    'define': 'def',
    "go": "pass",
    "generate_rstring": "grw",
    "send_to": "s_connect",
    "connect_to": "c_connect",
    "random_hide": "encrypt",
    'unhide': "decrypt",
    'greater_than': '>',
    'less_than': "<",
    '=or_greater_then': '>=',
    'create_graph': "make_graph"


}


def make_graph(columns, rows, data):
    graph = SimpleMake("graph")
    graph.make(columns, rows, data)
    graph.show()


def get(arg, item):
    if item.lower() == "graph":
        try:

            return graph.give(arg.lower())
        except Exception as e:
            return None



user = None
arg = False
read_this = ''
argument = ''
conversions = []
do = ''
rip = []

offset_value = random.randint(1, 5)


def randomized():
    return random.randint(1, 5) * random.randint(1, 9)**random.randint(0, 5)-random.randint(2, 30)


def offset(letter):
    unicode = ord(letter)
    letter = chr(unicode + offset_value)
    return letter


def reverse_offset(letter):
    unicode = ord(letter)
    letter = chr(unicode - offset_value)
    return letter


def encrypt(data):
    join_this = []
    return_this = None
    try:
        data = data.spilt()
    except Exception as e:
        data = data
    for i in range(len(data)):
        for character in data[i]:
            join_this.append(offset(data[i]))
    return_this = ''.join(join_this)
    return return_this


def decrypt(data):
    join_this = []
    return_this = None
    try:
        data = data.spilt()
    except Exception as e:
        data = data
    for i in range(len(data)):
        for character in data[i]:
            join_this.append(reverse_offset(data[i]))
    return_this = ''.join(join_this)
    return return_this


def grw(t):
    blank = ''.join(random.choice(string.ascii_lowercase) for _ in range(t))
    return blank


def s_connect(port):
    import socket

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind(("0.0.0.0", port))
    soc.listen(5)

    while True:
        client_socket, client_address = soc.accept()
        print(f"Connection from {client_address} has been established.")
        sending = True
        while sending:
            data = client_socket.recv(1024)
            if data:
                print("DATA: ", data)
            else:
                print("No data sent")
            sent = input("SEND: ")
            client_socket.send(sent.encode())


def c_connect(port):
    import socket

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind(("0.0.0.0", port))
    soc.listen(5)

    while True:
        client_socket, client_address = soc.accept()
        print(f"Connection from {client_address} has been established.")
        sending = True
        while sending:
            data = client_socket.recv(1024)
            if data:
                print("DATA: ", data)

            else:
                print("No data sent")
            sent = input("SEND: ")
            client_socket.send(sent.encode())


def turn():
    open('do_this', "w").close()
    file = open('read', "r")
    data = []
    for w in file:
        data.append(w.rstrip())
    for i in range(len(data)):
        for thing in dumbo_list_of_things:
            if thing in data[i]:
                key = dumbo_list_of_things.get(thing)
                data[i] = data[i].replace(thing, key)

    for tok in data:
        with open('do_this', 'a') as f:
            f.write(tok + "\n")
    with open('do_this', 'r') as fi:
        code = fi.read()
    exec(code)


while user != "q":
    user = input("> ")
    try:
        turn()
        offset_value = randomized()
    except Exception as e:
        print(e)
