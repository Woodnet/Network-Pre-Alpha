
#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter,time,sys
from cryptography.fernet import Fernet
from colorama import Fore,Style,init

#colors
init()
r = Style.BRIGHT + Fore.RED
g = Style.BRIGHT + Fore.GREEN
c = Style.BRIGHT + Fore.CYAN
w = Style.BRIGHT + Fore.WHITE
y = Style.BRIGHT + Fore.YELLOW
#
#encryption-decryption
key = input("Encrytion-Key>> ")
nickname = input("Nickname>> ")
f = Fernet(key.encode())
#

def receive():
    x = 0
    while True:
        try:
            x += 1
            new_msg = client_socket.recv(BUFSIZ)
            print(w+"["+g+"INFO"+w+"]"+g+" Verschlüsselte Nachricht wurde empfangen")
            sys.stdout.write(w+"\r["+g+"INFO"+w+"]"+g+" Nachricht wird entschlüsselt..")
            sys.stdout.flush()
            pkg = f.decrypt(new_msg)
            print(w+"ENTSCHLÜSSELT")
            msg = pkg.decode()
            try:
                msg_list.insert(tkinter.END,msg)
            except Exception:
                pass

        except OSError:
            break

def send(event=None):
    sys.stdout.write(w+"\r["+g+"INFO"+w+"]"+g+" Nachricht wird verschlüsselt..")
    sys.stdout.flush()
    msg = "%s"%(my_msg.get())
    my_msg.set("")
    pkt = msg.encode()
    packet = f.encrypt(pkt)
    print(w+"VERSCHLÜSSELT")
    client_socket.send(packet)
    if (msg == "+quit+"):
        print(w+"["+g+"INFO"+w+"]"+g+" Verbindung wird geschlossen")
        client_socket.close()
        top.quit()

def sendnickname(nickname):
    sys.stdout.write(w+"\r["+g+"INFO"+w+"]"+g+" Nickname wird verschlüsselt..")
    sys.stdout.flush()
    pkt = nickname.encode()
    packet = f.encrypt(pkt)
    print(w+"VERSCHLÜSSELT")
    client_socket.send(packet)
    if (nickname == "+quit+"):
        print(w+"["+g+"INFO"+w+"]"+g+" Verbindung wird geschlossen")
        client_socket.close()
        top.quit()
    

def on_closing(event=None):
    my_msg.set("+quit+")
    send()
    quit()

top = tkinter.Tk()
top.title("CHAT")
top.configure(bg="black")
top.geometry("1300x780")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)
h = tkinter.Label(top,bg="black")
h.pack()
msg_list = tkinter.Listbox(messages_frame,highlightbackground="black",height=25,width=140,
selectbackground="blue",font="Arial 13",fg="white",
bg="black",bd=0,
yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()
entry_field = tkinter.Entry(top, width=105,font="Courier 15",bg="white",
bd=1,highlightbackground="white",fg="black",textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.place(x=10,y=700)
#send_button = tkinter.Button(top,font="Arial 20",bg="gray18", fg="white",text="Senden", command=send)
#send_button.pack()
top.protocol("WM_DELETE_WINDOW", on_closing)
init()
HOST = "192.168.81.128" #"3.21.60.148"-Ngrok (default)
init()
print(w+"\n\n"+r+"CHAT"+g+"Client")
print(w+"--> Version 1.0 \n--> Autor: Pulsar\n\n")
PORT = 1330
sys.stdout.write(w+"\r["+g+"INFO"+w+"]"+g+" Verbindung wird zu"+w+" %s "%(HOST)+g+"über den Port "+w+"%s"%(PORT)+g+" hergestellt..")
sys.stdout.flush()
BUFSIZ = 1024
ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM) #tcp
try:
    client_socket.connect(ADDR)
    print(w+"VERBUNDEN")
except:
    print(r+"FEHLGESCHLAGEN")
    quit()
print(w+"["+g+"INFO"+w+"]"+w+" Eigene"+g+" AES-Verschlüsselung wird benutzt")
print(w+"["+g+"INFO"+w+"]"+g+" Sicherer Chatroom ist bereit")
print(w+"["+g+"INFO"+w+"]"+g+" Dein Nickname: %s"%(nickname))
sendnickname(nickname)
receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()
