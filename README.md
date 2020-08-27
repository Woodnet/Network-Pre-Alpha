# Network-Pre-Alpha
Eine Pre-Alpha-Version. Derzeit ist nur ein Chat-Server verfügbar, welcher mit dem Client über eine AES-256-Verschlüsselung kommuniziert.
# Pre-Alpha-Version?
D.h., dass die Scripts bei weitem noch nicht fertig sind. Die Webseite ist ein Beispiel und das Design wird 
noch verändert. Der Server aktzeptiert bis jetzt nur mit einem Client, also noch kein multithreading. 
Der Client kann über 2-Threads eine Nachricht senden und gleichzeitig an einem beliebigen Port auf eine verschlüsselte Nachricht vom 
Server warten.
# Achtung!
Der Server will die den Hostnamen "localhost" (IP: 127.0.0.1) mit dem Port 1337 binden. Stelle sicher, dass dieser nicht 
schon in Benutzung ist!
# Verwendete Python-Module 

      --> cryptography (Fernet)
      --> socket 
      --> datetime (datetime)
      --> colorama (Fore,init,Style)
      --> tkinter 
      --> ( Tkinter )

# Fehlende Module installieren
   
      pip install cryptography

# Linux-PIP-Fehler

      pip3 install cryptography

oder 

      sudo apt-get intall python3-pip
      pip3 install cryptography

 
