# Exercice 3 : Fonction Récursive
def somme_entiers(n):
    if n == 1:
        return 1
    else:
        return n + somme_entiers(n - 1)

n = 5
résultat = somme_entiers(n)
print(f"La somme des entiers de 1 à {n} est {résultat}.")
