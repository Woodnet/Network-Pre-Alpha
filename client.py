import os,sys,socket
from colorama import Fore,init,Style
from cryptography.fernet import Fernet
from datetime import datetime

def close_all():
    client.close()
    quit()

def gettime():
    n = datetime.now()
    now = "%s:%s:%s"%(n.hour,n.minute,n.second)
    return now

# colors
init()
w = Style.BRIGHT + Fore.WHITE
r = Style.BRIGHT + Fore.RED
c = Style.BRIGHT + Fore.CYAN
g = Style.BRIGHT + Fore.GREEN
y = Style.BRIGHT + Fore.YELLOW
#
# Encryption-Decryption
db_pwd = 'Schinken1981' # default
key = b'Ik02vkKf50SpuCRlKhGdj5xCI-KpOQ41J1D2fLS3Fv4=' # AES-Encryption
f = Fernet(key)

def sendpwd():
    pkg = encryption(db_pwd)
    try:
        client.send(pkg)
    except:
        close_all()
    try:
        pkg = client.recv(100)
        msg = decryption(pkg)
        if (msg == "Code16"):
            print("Correct")
        else:
            print("FALSE PWD")
            close_all()
    except:
        close_all()

def encryption(msg):
    sys.stdout.write("\r [%s] [INFO] Encrypting Message.." % (gettime()))
    sys.stdout.flush()
    try:
        encr_msg = f.encrypt(msg.encode())
        print(w+"["+g+"encrypted"+w+"]")
    except:
        print(w+"["+r+"failed"+w+"]")
        close_all()
    return encr_msg

def decryption(encr_msg):
    sys.stdout.write("\r [%s] [INFO] Decrypting Message.." % (gettime()))
    sys.stdout.flush()
    try:
        msg = f.decrypt(encr_msg)
        msg_new = msg.decode()
        print(w+"["+g+"decrypted"+w+"]")
    except Exception:
        print(w+"["+r+"failed"+w+"]")
        close_all()
    return msg_new
#
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP
db_addr = ("localhost",1334)
sys.stdout.write(w+"\r Connecting to Database..")
sys.stdout.flush()
try:
    client.connect(db_addr)
    print(g+"CONNECTED")
except socket.error:
    print(r+"FAILED")
    client.close()
    quit()
sendpwd()
print("\n\n <=Physik-Database=>\n\n")
print(w+"Type"+c+" help"+w+" for Help\n")
while True:
    command = input(r+"@physik_database$ ")
    if (command == "cls" or command == "clear"):
        os.system("cls") # Windows | default
    if (command == "finalshdown"):
        msg = "Code18"
        pkg = encryption(msg)
        try:
            client.send(pkg)
        except:
            pass
        close_all()
    if (command == "closeconnection"):
        msg = "Code14"
        pkg = encryption(msg)
        try:
            client.send(pkg)
        except:
            pass
        close_all()
    if (command == "help"):
        try:
            pkg = encryption(command)
            client.send(pkg)
        except:
            close_all()
    if (command == "download"):
        filename = input("Filename: ")
        try:
            pkg = encryption(filename)
            try:
                client.send(pkg)
            except:
                close_all()
        except:
            close_all()
        try:
            pkg = client.recv(2048)
            msg = decryption(pkg)
        except:
            close_all()
        print(w+"\n%s\n"%(msg))
        if (msg == "This file does not exist!"):
            print(w+"\n%s\n"%(msg))
        else:
            try:
                newfile = open(filename,"w")
                newfile.write(msg)
                newfile.close()
            except:
                close_all()
            print(" [INFO] Downloaded %s" % (filename))

    if (command == "upload"):
        filename = input("Filename: ")
        try:
            pkg = encryption(filename)
            try:
                client.send(pkg)
            except:
                close_all()
        except:
            close_all()
        try:
            openfile = open(filename,"r")
            crash = False
        except:
            print(r+"This file does not exist!")
            crash = True
        if (crash == True):
            pass
        else:
            content = openfile.read()
            openfile.close()
            try:
                pkg = encryption(content)
                client.send(pkg)
            except socket.error:
                close_all()
            try:
                pkg = client.recv(2048)
            except:
                close_all()
            msg = decryption(pkg)
            print(w+"\n%s\n" % (msg))
            try:
                pkg = client.recv(2048)
            except:
                close_all()
            msg = decryption(pkg)
            print(w+"\n%s\n" % (msg))

    if (command == "sh all files"):
        try:
            msg = "sh all files"
            pkg = encryption(msg)
            client.send(pkg)
        except:
            close_all()
        print(w+"Receiving all Filenames..")
        try:
            pkg = client.recv(2048)
        except:
            close_all()
        msg = decryption(pkg)
        print("\n%s\n" % (msg))


    else:
        pkg = encryption(command)
        try:
            client.send(pkg)
        except:
            print(r+"\nError. Connection down.")
            close_all()
        try:
            pkg = client.recv(2048)
            msg = decryption(pkg)
        except:
            print(r+"\nError. Connection down.")
            close_all()
        print(w+"\n%s\n" % (msg))




