# Definir la classe des produits
class Produit:
    def __init__(self, nom, quantité, prix):
        self.nom = nom
        self.quantité = quantité
        self.prix = prix

class Inventaire:
    def __init__(self):
        self.produits = []

    def ajouter_produit(self, produit):
        self.produits.append(produit)

    def afficher_inventaire(self):
        for produit in self.produits:
            print(f"Nom : {produit.nom}, Quantité : {produit.quantité}, Prix : {produit.prix}")

    def valeur_totale_inventaire(self):
        total = sum(produit.quantité * produit.prix for produit in self.produits)
        return total

# Utilisation de la classe Inventaire
inventaire = Inventaire()
produit1 = Produit("Livre", 10, 15)
produit2 = Produit("Stylo", 100, 1)

inventaire.ajouter_produit(produit1)
inventaire.ajouter_produit(produit2)
inventaire.afficher_inventaire()

valeur_totale = inventaire.valeur_totale_inventaire()
print(f"Valeur totale de l'inventaire : {valeur_totale} €")
