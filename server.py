import socket, threading, random

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientAddress = clientAddress
        print ("Conexiuna noua: ", self.clientAddress)
    
    def run(self):
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            print ("Mesaj: ", msg, " de la clientul: ", self.clientAddress)

            if msg == '':
                break
            elif msg.upper() == "START":
              self.cifru = random.randint(1, 100)
              self.numar_incercari = 0
              self.csocket.send(bytes("GHICESTE",'utf-8'))
            elif int(msg) > self.cifru:
              self.csocket.send(bytes("PREA MARE! ÎNCEARCĂ DIN NOU",'utf-8'))
              self.numar_incercari += 1
            elif int(msg) < self.cifru:
              self.csocket.send(bytes("PREA MIC! ÎNCEARCĂ DIN NOU",'utf-8'))
              self.numar_incercari += 1
            else:
              self.csocket.send(bytes("AI GHICIT DIN " + str(self.numar_incercari) + " INCERCĂRI",'utf-8'))    
            
        print ("Clientul de la adresa: ", self.clientAddress , " s-a deconectat...")


LOCALHOST = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))

print("Server pornit si gata de joc")

while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()  