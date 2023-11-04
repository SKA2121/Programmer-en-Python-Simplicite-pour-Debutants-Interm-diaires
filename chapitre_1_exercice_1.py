# Exercice 1 : Ma première calculatrice
def calculatrice():
    
    # definissons les variables qui seront fournies par l'utilisateur
    
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le deuxième nombre : "))
    operateur = input("Entrez l'operateur (+, -, *, /) : ")
    
    
    # Etablissement des conditions

    if operateur == "+":
        résultat = a + b
    elif operateur == "-":
        résultat = a - b
    elif operateur == "*":
        résultat = a * b
    elif operateur == "/":
        résultat = a / b
    else:
        résultat = "operateur invalide"

 # On affiche les resultats
    print("Résultat :", résultat)

 # Appel de la fonction
calculatrice()
