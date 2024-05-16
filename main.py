import random
import string
import turtle
import pygame
import time
import math
from simple_make import SimpleMake


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
    'create_graph': "make_graph",
    "log": 'math.log10',
    "with": "(",
    ".": ")"
}


def make_graph(columns, rows, data):
    graph = SimpleMake("graph")
    graph.make(columns, rows, data)
    graph.show()
    return graph


def get(arg_, item, object):
    if item.lower() == "graph":
        if arg_ == "avg":
            return object(arg_.lower())


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


pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Shoot the Fruit!")

# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
text_box = pygame.Rect(95, 200, 150, 32)
screen = pygame.display.set_mode(size)


r = 200
g = 255
b = 100

# render the text for later
message = "Click the fruit to score!"
display_message = my_font.render(message, True, (255, 255, 255))

lines = {1: ""}

run = True
user_input = ""
display_input = my_font.render(user_input, True, (255, 255, 255))
show_input = ""
# -------- Main Program Loop -----------
while run:
    i = 1
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SEMICOLON:
                file = open('read', "w")
                with open("read", "w") as f:
                    f.write(user_input)
                turn()
            elif event.key == pygame.K_RETURN:
                print("d")
                user_input += ""
                lines[i +1] = None
                i += 1
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
                print("h")
            else:
                user_input += event.unicode
                lines[i] = user_input
            for x in range(len(lines)):
                try:
                    show_input += lines[x + 1] + '\n'
                except Exception as TypeError:
                    pass
            display_input = my_font.render(show_input, True, (255, 255, 255))
    screen.fill((200, 200, 200))
    screen.blit(display_message, (0, 0))
    screen.blit(display_input, (text_box.x + 5, text_box.y + 5))
    text_box.w = max(100, display_input.get_width() + 10)
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
