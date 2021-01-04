import socket

SERVER = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

print("Incepe jocul")

while True:
  out_data = input()
  if out_data == 'bye':
    break
  client.sendall(bytes(out_data,'UTF-8'))
  in_data =  client.recv(1024)
  print("Mesaj de la server:", in_data.decode())
 
client.close()