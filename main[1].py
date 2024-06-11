import random
import string
import turtle
import pygame
import time
import math
#: For users use/ I.e. if they want to exec features from time or math
import sys
from simple_make import SimpleMake
from button import Button
from menu import Menu


list_of_things = {
    'run_if': 'while',
    'show': 'print',
    'execute': ':',
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


def display_lines(surface, text, font, color, location):
    h = font.get_height()
    x, y = location
    multi_text = text.split("|")
    for i, words in enumerate(multi_text):
        num = str(i + 1)
        text_surface = font.render(words, True, color)
        number_of_line = font.render(num, True, (100, 200, 10))
        surface.blit(text_surface, (x, (y + (i*h))))
        surface.blit(number_of_line, (x - 30, (y + i*h)))


def line_to_exec(txt):
    text = txt.split("|")
    string_blank = '\n'. join(text)
    return string_blank


def string_to_display(list_):
    s = '|'
    print(list_)
    s = s.join(list_)
    return s


def make_graph(columns, rows, data):
    graph = SimpleMake("graph")
    graph.make(columns, rows, data)
    graph.show()
    return graph


def get(arg_, item, object_):
    if item.lower() == "graph":
        if arg_ == "avg":
            return object_(arg_.lower())


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
    except Exception as a_error:
        data = data
        print(a_error)
    for i in range(len(data)):
        join_this.append(offset(data[i]))
    return_text = ''.join(join_this)
    return return_text


def decrypt(data):
    join_this = []
    try:
        data = data.spilt()
    except Exception as error:
        data = data
        print(error)
    for i in range(len(data)):
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


def start():
    open('execute', "w").close()
    file_to_read = open('read', "r")
    data = []
    for w in file_to_read:
        data.append(w.rstrip())
    for i in range(len(data)):
        for thing in list_of_things:
            if thing in data[i]:
                key = list_of_things.get(thing)
                data[i] = data[i].replace(thing, key)

    for token in data:
        with open('execute', 'a') as f_:
            f_.write(token + "\n")
    with open('execute', 'r') as fi:
        code = fi.read()
    exec(code)




pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("SimpleTxT")

# set up variables for the display
SCREEN_HEIGHT = 750
SCREEN_WIDTH = 750
size = (SCREEN_WIDTH, SCREEN_HEIGHT)

text_box = pygame.Rect(200, 200, 150, 32)
screen = pygame.display.set_mode(size)


r = 200
g = 255
b = 100

# render the text for later
message = ""
display_message = my_font.render(message, True, (255, 255, 255))

lines = {1: ""}

run = True
user_input = ""
display_input = my_font.render(user_input, True, (255, 255, 255))
show_input = ""
placeholder = ''
index = 1
position = 1
left_pressed = 0
pos_last = True
button = Button(15, 20)
menu_1 = Menu(1, 650, "----> Guide", screen)
menu_open = False
number_line = ""
output = ""
welcome = 'Welcome to SimpleTxt now with Tkinter and Plots'
typeable = True
# -------- Main Program Loop -----------
while run:
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()
    offset_value = random.randint(1, 5)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.rect.collidepoint(mouse):
                button.switch_image()
                file = open('read', "w")
                with open("read", "w") as f:
                    f.write((line_to_exec(show_input)))
                start()
            if menu_1.rect.collidepoint(mouse):
                menu_open = not menu_open

        if position == 0 or position == len(user_input):
            pos_last = True
        else:
            pos_last = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if position > 1:
                    position -= 2
                    pos_last = False
            if event.key == pygame.K_RIGHT:
                if position != len(user_input):
                    position += 2

            if event.key == pygame.K_SEMICOLON:
                file = open('read', "w")
                typeable = False
                with open("read", "w") as f:
                    f.write((line_to_exec(show_input)))
                start()
            elif event.key == pygame.K_RETURN:
                user_input = ""
                lines[index + 1] = ""
                index += 1
                position = 1
                typeable = False

            elif event.key == pygame.K_BACKSPACE:
                pos = position - 1
                user_input = user_input[:(position - 1)]
                lines[index] = lines[index][:pos]
                typeable = False
                if position > 1:
                    position -= 1

            elif event.key == pygame.K_UP:
                if (index - 1) != 0:
                    up_line = True
                    index -= 1
                    user_input = lines[index]
                    position = len(user_input)
                    if len(user_input) == 0:
                        position = 1
                    typeable = False

            elif event.key == pygame.K_DOWN:
                try:
                    if lines[index + 1]:
                        index += 1
                        user_input = lines[index]
                        position = len(user_input)
                except Exception as KeyError:
                    lines[index + 1] = ""
                    index += 1
                    user_input = ""
                typeable = False

            if pos_last and typeable:
                user_input += event.unicode
                position += 1
                lines[index] = user_input

            elif not pos_last and typeable:
                user_input_spilt = [x for x in user_input]
                if event.unicode != "":
                    user_input_spilt.insert(position, event.unicode)
                    user_input = "".join(user_input_spilt)
                    lines[index] = user_input
                    print(position)
                    position += 1

            for x in range(len(lines)):
                try:
                    placeholder = ""
                    placeholder += lines[index]
                except Exception as e:
                    print(e)

        lines_txt = list(lines.values())
        show_input = string_to_display(lines_txt)
    welcome_display = my_font.render(welcome, True, (255, 255, 255))
    typeable = True
    screen.fill((35, 35, 35))
    if menu_open:
        print("menu")
        menu_1.open(screen)
    screen.blit(menu_1.image, menu_1.rect)
    screen.blit(welcome_display, (470, 720))
    screen.blit(button.image, button.rect)
    screen.blit(display_message, (0, 0))
    display_lines(screen, show_input, my_font, (255, 255, 0), (100, 20))

    pygame.display.flip()
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
