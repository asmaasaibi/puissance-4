# puissance4.py

# Créer une grille vide (6 lignes, 7 colonnes)
def creer_grille():
    return [["." for _ in range(7)] for _ in range(6)]

# Afficher la grille joliment
def afficher_grille(grille):
    for ligne in grille:
        print(" ".join(ligne))
    print("0 1 2 3 4 5 6")  # pour savoir quelle colonne choisir

# Test
grille = creer_grille()
afficher_grille(grille)
