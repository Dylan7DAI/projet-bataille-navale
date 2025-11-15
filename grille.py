# grille.py

class Grille:
    def __init__(self, n_lignes: int, n_colonnes: int):
        """Créer une grille remplie de '.' """
        self.n_lignes = n_lignes
        self.n_colonnes = n_colonnes
        self.vide = '.'
        self.tir = 'x'   # tir dans l'eau

        # matrice stockée dans une liste simple
        self.matrice = [self.vide] * (n_lignes * n_colonnes)

    def index(self, ligne: int, colonne: int) -> int:
        """Convertit (ligne, colonne) en index dans la liste"""
        return (ligne - 1) * self.n_colonnes + (colonne - 1)

    def afficher(self):
        """Affiche la grille proprement"""
        for i in range(self.n_lignes):
            début = i * self.n_colonnes
            fin = début + self.n_colonnes
            ligne = self.matrice[début:fin]
            print(" ".join(ligne))

    def tirer(self, x: int, y: int):
        """Tire sur la case (x, y). Pour l’instant : toujours raté."""
        i = self.index(x, y)
        self.matrice[i] = self.tir

    
    def __str__(self):
        lignes = []
        for l in range(self.n_lignes):
            début = l * self.n_colonnes
            fin = début + self.n_colonnes
            ligne = "".join(self.matrice[début:fin])
            lignes.append(ligne)
        return "\n".join(lignes)

