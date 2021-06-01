#
#By Pulsar
#Python-Version: 3 (7.2)
#Script: Main-Server
#
import socket,os,sys 
from datetime import datetime 
from cryptography.fernet import Fernet 
from threading import Thread

os.system("clear") #Linux -default

def gettime():
    n = datetime.now()
    now = "%s:%s:%s"%(n.hour,n.minute,n.second)
    return now 

def failure(e):
    #
    message = '<td class="redtext">%s</td><!--Server_Failure_ErrorCode-->'%(e)
    keyword = "Server_Failure_ErrorCode"
    writeinfile(filename,message,keyword)
    #
    message = '<td class="redtext">Connection Down</td><!--Server_Status_NOW_CURRENT-->'
    keyword = "Server_Status_NOW_CURRENT"
    writeinfile(filename,message,keyword)
    quit()
    #

def testfile(filename):
    sys.stdout.write(" [%s] [INFO] Testing %s -File.."%(gettime(),filename))   
    sys.stdout.flush()
    try:
        file = open(filename, "r")
        file.close()
        print("[+]")
    except:
        print("[!] The File does not exist!")
        quit()

def accept_incoming_connections(s,filename,m,connections):
    while True:
        client, client_address = s.accept()
        connections += 1
        print(" [%s] [INFO] Neue Verbindung wurde hinzugefügt"%(gettime()))
        message = '<td class="messagetext">%s</td><!--Connected_Number-->'%(connections)
        keyword = "Connected_Number"
        writeinfile(filename,message,keyword)
        #client.send(bytes("Willkommen beim Woodnet Chatroom! Gebe bitte deinen gewuenschten Namen ein und druecke Enter", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,s,filename,m,connections)).start()

def encryption(msg):
    f = Fernet(key)
    sys.stdout.write(" [%s] [INFO] Encrypting Message.."%(gettime()))   
    sys.stdout.flush()
    try:
        packet = f.encrypt(msg.encode())
        print("[+]")
    except Exception as e:
        print("[!]")
        failure(e)
    return packet 

def decryption(packet):
    f = Fernet(key)
    sys.stdout.write(" [%s] [INFO] Decrypting Message.."%(gettime()))   
    sys.stdout.flush()
    try:
        msg = f.decrypt(packet)
        print("[+]")
    except Exception as e:
        print("[!]")
        failure(e)
    return msg.decode()

def writeinfile(filename,message,keyword):
    file = open(filename,"r")
    Lines = file.readlines()
    x = 0
    for line in Lines:
        x += 1
        if (keyword in line.strip()):
            x -= 1
            Lines[x] = "%s\n"%(message)
            out = open(filename, 'w')
            out.writelines(Lines)
            out.close()
            file.close()
            break
        else:
            pass 

def create_socket(s,s_addr,filename):
    sys.stdout.write(" [%s] [INFO] Binding Address..."%(gettime()))   
    sys.stdout.flush()
    message = '<td class="yellowtext">Binding Address</td><!--Server_Status_NOW_CURRENT-->'
    keyword = "Server_Status_NOW_CURRENT"
    writeinfile(filename,message,keyword)
    try:
        s.bind(s_addr)
        print("[+]")
    except Exception as e:
        print("[!]")
        failure(e)

def client_close(client,connections,name,m):
    del clients[client]
    print(" [%s] [WARNUNG] %s hat den Chat verlassen." %(gettime(),name))
    message = '<td class="greentext">Connected</td><!--Server_Status_NOW_CURRENT-->'
    keyword = "Server_Status_NOW_CURRENT"
    writeinfile(filename,message,keyword)
    broadcast("Hat den Chat verlassen",name)
    m += 1
    message = '<td class="messagetext">%s</td><!--Sent_Messages-->'%(m)
    keyword = "Sent_Messages"
    writeinfile(filename,message,keyword)
    client.close()
    connections -= 1
    message = '<td class="messagetext">%s</td><!--Connected_Number-->'%(connections)
    keyword = "Connected_Number"
    writeinfile(filename,message,keyword)
    quit()

def handle_client(client,s,filename,m,connections): 
    message = '<td class="greentext">Connected</td><!--Server_Status_NOW_CURRENT-->'
    keyword = "Server_Status_NOW_CURRENT"
    writeinfile(filename,message,keyword)
    try:
        packet = client.recv(2048)
        name = decryption(packet)
    except:
        client_close(client,connections)
    welcome = 'Willkommen %s! Wenn du den Chat verlassen willst gebe bitte +quit+ ein.'%(name)
    packet = encryption(welcome)
    try:
        client.send(packet)
    except:
        client_close(client,connections)
    m += 1
    message = '<td class="messagetext">%s</td><!--Sent_Messages-->'%(m)
    keyword = "Sent_Messages"
    writeinfile(filename,message,keyword)
    msg = "ist dem Chat beigetreten"
    broadcast(msg,name)
    m += 1
    message = '<td class="messagetext">%s</td><!--Sent_Messages-->'%(m)
    keyword = "Sent_Messages"
    writeinfile(filename,message,keyword)
    clients[client] = name
    while True:
        m += 1
        packet = client.recv(2048)
        msg = decryption(packet)
        if (msg != "+quit+"):
            broadcast(msg, name)
            message = '<td class="messagetext">%s</td><!--Sent_Messages-->'%(m)
            keyword = "Sent_Messages"
            writeinfile(filename,message,keyword)
        else:
            client_close(client,connections,name,m)

def broadcast(msg, prefix):
    for sock in clients:
        message = "<%s> %s"%(prefix,msg)
        packet = encryption(message)
        sock.send(packet)

#MAIN-HOME
key = Fernet.generate_key()
filename = "changeindex.html"
message = '<td class="text"><input type="text" value="%s" id="encryptionkey"></td><!--Server_Encryption_Key-->'%(key.decode())
keyword = "Server_Encryption_Key"
writeinfile(filename,message,keyword)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP 
s_addr = ("0.0.0.0",1330)
m = 0
connections = 0
clients = {}
addresses = {}
def cl():
    message = '<td class="redtext">Connection Down</td><!--Server_Status_NOW_CURRENT-->'
    keyword = "Server_Status_NOW_CURRENT"
    writeinfile(filename,message,keyword)
    message = '<td class="redtext">-</td><!--Server_Failure_ErrorCode-->'
    keyword = "Server_Failure_ErrorCode"
    writeinfile(filename,message,keyword)
    message = '<td class="messagetext">-</td><!--Connected_Number-->'
    keyword = "Connected_Number"
    writeinfile(filename,message,keyword)
    message = '<td class="messagetext">0</td><!--Sent_Messages-->'
    keyword = "Sent_Messages"
    writeinfile(filename,message,keyword)
cl()

if __name__ == "__main__":
    try:
        testfile(filename)
        create_socket(s,s_addr,filename)
        print(" [%s] [INFO] Listening for Clients.."%(gettime()))   
        message = '<td class="yellowtext">Listening for Clients..</td><!--Server_Status_NOW_CURRENT-->'
        keyword = "Server_Status_NOW_CURRENT"
        writeinfile(filename,message,keyword)
        s.listen(5)
        ACCEPT_THREAD = Thread(target=accept_incoming_connections,args=(s,filename,m,connections))
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
        s.close()
        message = '<td class="redtext">Connection Down</td><!--Server_Status_NOW_CURRENT-->'
        keyword = "Server_Status_NOW_CURRENT"
        writeinfile(filename,message,keyword)
    except KeyboardInterrupt:
        cl()
        quit() 
#
