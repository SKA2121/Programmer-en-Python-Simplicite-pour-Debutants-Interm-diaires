# Exercice 2 : Gestion d'un Dictionnaire
carnet_adresses = {}

# Fonction pour l'ajout d'un contact
def ajouter_contact(nom, numéro):
    carnet_adresses[nom] = numéro

# Supprimer un contact s'il existe déjà dans le dictionnaire
def supprimer_contact(nom):
    if nom in carnet_adresses:
        del carnet_adresses[nom]

# Afficher les contacts
def afficher_contacts():
    for nom, numéro in carnet_adresses.items():
        print(f"{nom} : {numéro}")


# Appel des fonctions
ajouter_contact("Alice", "555-1234")
ajouter_contact("Bob", "555-5678")

afficher_contacts()

supprimer_contact("Bob")
afficher_contacts()
