# Serveur
import socket

# Créez un socket serveur
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liez le socket à une adresse et un port
serveur.bind(('0.0.0.0', 12345))

# Écoutez les connexions entrantes
serveur.listen(5)

while True:
    # Acceptez la connexion
    client, adresse = serveur.accept()
    print(f'Connexion depuis {adresse}')

    # Recevez et envoyez des données
    client.send(b'Bienvenue sur le serveur de chat !')
    data = client.recv(1024)
    print(f'Client dit : {data.decode()}')

    # Fermez la connexion
    client.close()