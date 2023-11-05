class Plat:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

class Commande:
    def __init__(self):
        self.plats = []

    def ajouter_plat(self, plat, quantité=1):
        self.plats.append((plat, quantité))

    def calculer_total(self):
        total = sum(plat.prix * quantité for plat, quantité in self.plats)
        return total

    def afficher_facture(self):
        print("Facture de la commande :")
        for plat, quantité in self.plats:
            print(f"{plat.nom} x{quantité} : {plat.prix * quantité} €")
        total = self.calculer_total()
        print(f"Total : {total} €")

# Utilisation de la classe Commande
commande = Commande()
pizza = Plat("Pizza", 12.50)
pâtes = Plat("Pâtes", 8.75)

commande.ajouter_plat(pizza, 2)
commande.ajouter_plat(pâtes, 1)

commande.afficher_facture()
