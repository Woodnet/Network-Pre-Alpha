# Network-Pre-Alpha
Eine Pre-Alpha-Version. Derzeit ist nur ein Chat-Server verfügbar, welcher mit dem Client kommuniziert.
# Verschlüsselung? 
Die Kommunikation erfolgt über das Python-Modul cryptography und benutzt eine sichere AES-256-Verschlüsselung.
Der Schlüssel wird immer unmittelbar nach dem Start des Server-Scripts zufällig generiert. 

So sieht der Schlüssel in etwa aus: g0pp5rQujpQR5CekO6zXjvp1ecRjV9i_huA6KgJHed0=

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

 # Wie führe ich das Script aus? (Windows)
 
1. Öffne die Konsole

            python3 REPserver.py 
 
2. Öffne eine zweite Konsole oder einen neuen Reiter

            python3 REPclient.py

3. Downloade Ngrok:
            
            Ngrok-ZIP-Installation: https://ngrok.com/download
            
            Ein YouTube-Video zur Installation: https://www.youtube.com/watch?v=9gaaVbX0USI
            
      
      

4. Öffne anhand von Ngrok den HTTP-Port 80

5. Gebe in den Browser diese Adresse ein:

            http://localhost/

 # Wie führe ich das Script aus? (Linux)
 
 1. Öffne die Konsole
      
            python3 REPserver.py
 
 2. Öffne eine zweite Konsole oder einen neuen Reiter
      
            python3 REPclient.py
 
 3. Öffne eine dritte Konsole oder einen neuen Reiter
            
            service apache2 start
            
 4. Sollte dieser Dienst nicht vorhanden sein, dann gebe in der Konsole ein
 
            sudo apt-get install apache2
            
            oder 
            
            sudo apt-get install apache
            
            dann 
            
            sudo service apache2 start
            
 5. Gebe in der Konsole ein
 
            sudo service apache2 status
            
 6. Öffne den Browser 
 
            http://localhost/
          
            
                  


      
