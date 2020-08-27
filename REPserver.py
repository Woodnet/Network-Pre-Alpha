import socket,os,sys 
from datetime import datetime 
from cryptography.fernet import Fernet 

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

def encryption(key,msg,filename):
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

def decryption(key,packet):
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

def send_msg(client,packet):
    sys.stdout.write(" [%s] [INFO] Sending Message.."%(gettime()))   
    sys.stdout.flush()
    try:
        client.send(packet)
        print("[+]")
    except Exception as e:
        print("[!]")
        failure(e)

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

def run_server(s,filename,m):
    sys.stdout.write(" [%s] [INFO] Listening for Client.."%(gettime()))   
    sys.stdout.flush()
    message = '<td class="yellowtext">Listening for Client..</td><!--Server_Status_NOW_CURRENT-->'
    keyword = "Server_Status_NOW_CURRENT"
    writeinfile(filename,message,keyword)
    s.listen(1)
    (client,addr) = s.accept()
    message = '<td class="greentext">Connected</td><!--Server_Status_NOW_CURRENT-->'
    keyword = "Server_Status_NOW_CURRENT"
    writeinfile(filename,message,keyword)
    message = '<td class="greentext">%s</td><!--Client_Address_Connected-->'%(str(addr))
    keyword = "Client_Address_Connected"
    writeinfile(filename,message,keyword)
    print("[+]")
    message = "Hello Client! You are now connected with the Server!"
    packet = encryption(key,message,filename)
    sys.stdout.write(" [%s] [INFO] Sending Message to Client.."%(gettime()))   
    sys.stdout.flush()
    m += 1
    message = '<td class="text">%s</td><!--Sent_Messages-->'%(m)
    keyword = "Sent_Messages"
    writeinfile(filename,message,keyword)
    send_msg(client,packet)
    while True:
        sys.stdout.write(" [%s] [INFO] Receiving Packet.."%(gettime()))   
        sys.stdout.flush()
        try:
            packet = client.recv(2048)
            m += 1
            print("[+]")
            message = '<td class="senttext">%s</td><!--Sent_Messages-->'%(m)
            keyword = "Sent_Messages"
            writeinfile(filename,message,keyword)
        except Exception as e:
            print("[!]")
            failure(e)  
        message = decryption(key,packet)
        newmessage = "<[CLIENT]> %s"%(message)
        packet = encryption(key,message,filename)
        send_msg(client,packet)
        print(" <[CLIENT]> %s"%(message))
        message = '<td class="messagetext">%s</td><!--Last_Message_CURRENT-->'%(len(packet.decode()))
        keyword = "Last_Message_CURRENT"
        writeinfile(filename,message,keyword)
        

#MAIN-HOME
key = Fernet.generate_key()
filename = "chatindex.html"
message = '<td class="text"><input type="text" value="%s" id="encryptionkey"></td><!--Server_Encryption_Key-->'%(key.decode())
keyword = "Server_Encryption_Key"
writeinfile(filename,message,keyword)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP 
s_addr = ("localhost",1337)
m = 0
while True:
    try:
        testfile(filename)
        create_socket(s,s_addr,filename)
        run_server(s,filename,m)
    except KeyboardInterrupt:
        False 
s.close()
message = '<td class="redtext">Connection Down</td><!--Server_Status_NOW_CURRENT-->'
keyword = "Server_Status_NOW_CURRENT"
writeinfile(filename,message,keyword)
client.close()
quit()
    
#
        
        
        


        