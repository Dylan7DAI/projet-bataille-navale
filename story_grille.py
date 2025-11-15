# story_grille.py
# User Story : "Plouf dans l'eau"

from grille import Grille

# 1. créer une grille 5 x 8
g = Grille(5, 8)

while True:
    # 2. afficher la grille
    g.afficher()
    print()

    # 3. demander x,y

    print("\nEntrez une case :")
    try:
        x = int(input("ligne : "))
        y = int(input("colonne : "))
    # 4. tirer
        g.tirer(x, y)
    except IndexError:
        print("Veuillez entrer des nombres valides !")
        continue  # 如果输入无效，重新输入

    

    # 5. retour au début → la boucle while recommence
