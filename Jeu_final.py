# main.py
# Jeu de bataille navale simple
# Grille 8 x 10, 4 bateaux (un de chaque type)

import random

from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin, Bateau


def placements_possibles(grille: Grille, cls_bateau, occupees: set):
    """
    Renvoie toutes les positions possibles (ligne, colonne, vertical)
    pour un bateau de type cls_bateau, sachant :
      - il doit rester entièrement dans la grille
      - il ne doit pas se chevaucher avec les cases déjà occupées (occupees)
    """
    options = []
    for vertical in (False, True):
        for l in range(1, grille.n_lignes + 1):
            for c in range(1, grille.n_colonnes + 1):
                b = cls_bateau(l, c, vertical)
                positions = b.positions

                # vérifie que toutes les cases sont dans la grille
                if not all(grille._dans_grille(li, co) for (li, co) in positions):
                    continue

                # vérifie qu'il n'y a pas de chevauchement
                if any((li, co) in occupees for (li, co) in positions):
                    continue

                options.append((l, c, vertical))
    return options


def placer_bateaux_aleatoirement(grille: Grille) -> list:
    """
    Crée une liste de 4 bateaux (un de chaque type) placés aléatoirement
    sur la grille, sans chevauchement.
    Les bateaux ne sont PAS dessinés sur la grille au départ : la grille
    ne contient que de l'eau '~'. On les révélera quand ils seront coulés.
    """
    bateaux: list[Bateau] = []
    occupees: set = set()

    types = [PorteAvion, Croiseur, Torpilleur, SousMarin]

    for cls in types:
        options = placements_possibles(grille, cls, occupees)
        if not options:
            raise RuntimeError("Pas de placement possible pour ce bateau !")

        l, c, vertical = random.choice(options)
        b = cls(l, c, vertical)
        bateaux.append(b)

        # on réserve les cases occupées par ce bateau
        for pos in b.positions:
            occupees.add(pos)

    return bateaux


def tous_coules(bateaux: list, grille: Grille) -> bool:
    """True si tous les bateaux de la liste sont coulés."""
    return all(b.coule(grille) for b in bateaux)


def trouver_bateau_touche(bateaux: list, x: int, y: int):
    """Renvoie le bateau touché en (x, y) s'il y en a un, sinon None."""
    for b in bateaux:
        if (x, y) in b.positions:
            return b
    return None


def boucle_de_jeu():
    # 1. créer la grille et les bateaux
    grille = Grille(8, 10)
    bateaux = placer_bateaux_aleatoirement(grille)

    coups = 0  # nombre de tirs effectués

    print("Bienvenue dans la bataille navale !")
    print("Grille 8 x 10, 4 bateaux à couler.\n")

    # 2. boucle de gameplay
    while not tous_coules(bateaux, grille):
        print(grille)
        print()

        # lecture des coordonnées
        try:
            x = int(input("Ligne (1-8)   : "))
            y = int(input("Colonne (1-10): "))
        except ValueError:
            print("Veuillez entrer des entiers.")
            print()
            continue

        if not grille._dans_grille(x, y):
            print("Case en dehors de la grille, recommencez.\n")
            continue

        index_case = grille.index(x, y)
        # déjà tiré sur cette case ?
        if grille.matrice[index_case] in (grille.manque, grille.tir):
            print("Vous avez déjà tiré sur cette case, choisissez-en une autre.\n")
            continue

        coups += 1

        # 3. vérifier s'il y a un bateau sur cette case
        bateau_touche = trouver_bateau_touche(bateaux, x, y)

        if bateau_touche is None:
            # tir dans l'eau
            grille.tirer(x, y, grille.manque)
            print("À l'eau...\n")
        else:
            # tir sur un bateau
            grille.tirer(x, y, grille.tir)
            print("Touché !")

            # vérifier si le bateau est coulé
            if bateau_touche.coule(grille):
                print("Coulé :", type(bateau_touche).__name__)
                # on révèle le bateau en remplaçant les 💣 par sa marque
                for (lx, ly) in bateau_touche.positions:
                    idx = grille.index(lx, ly)
                    grille.matrice[idx] = bateau_touche.marque
                print()

            else:
                print()

    # 4. fin de partie
    print(grille)
    print(f"Bravo ! Vous avez coulé tous les bateaux en {coups} coups.")


if __name__ == "__main__":
    boucle_de_jeu()
