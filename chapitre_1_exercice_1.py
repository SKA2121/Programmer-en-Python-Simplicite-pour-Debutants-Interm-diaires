# Exercice 1 : Ma première calculatrice
def calculatrice():
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le deuxième nombre : "))
    operateur = input("Entrez l'operateur (+, -, *, /) : ")

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

    print("Résultat :", résultat)

calculatrice()
