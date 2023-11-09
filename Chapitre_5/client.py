# Client
import socket

# Créez un socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connectez-vous au serveur
client.connect(('127.0.0.1', 12345))

# Recevez et envoyez des données
data = client.recv(1024)
print(f'Serveur dit : {data.decode()}')
client.send(b'Hello, serveur !')

# Fermez la connexion
client.close()
