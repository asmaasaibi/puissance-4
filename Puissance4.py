# puissance4.py


def creer_grille():
    return [["." for _ in range(7)] for _ in range(6)]

def afficher_grille(grille):
    for ligne in grille:
        print(" ".join(ligne))
    print("0 1 2 3 4 5 6")

def ajouter_pion(grille, col, joueur):
    for ligne in reversed(grille):
        if ligne[col] == ".":
            ligne[col] = joueur
            return True
    return False

def changer_joueur(joueur):
    return "O" if joueur == "X" else "X"

def main():
    grille = creer_grille()
    joueur = "X"
    while True:
        afficher_grille(grille)
        try:
            col = int(input(f"Joueur {joueur}, choisis une colonne (0-6) : "))
            if 0 <= col < 7:
                if ajouter_pion(grille, col, joueur):
                    joueur = changer_joueur(joueur)
                else:
                    print("Colonne pleine, essaie une autre.")
            else:
                print("Choix invalide.")
        except ValueError:
            print("Entrée invalide. Tape un chiffre entre 0 et 6.")

if __name__ == "__main__":
    main()

