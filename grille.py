# grille.py

class Grille:
    def __init__(self, n_lignes: int, n_colonnes: int):

        self.n_lignes = n_lignes
        self.n_colonnes = n_colonnes
        self.vide = '~'
        self.manque = 'x'
        self.tir = '💣'   # tir dans l'eau


        # matrice stockée dans une liste simple
        self.matrice = [self.vide] * (n_lignes * n_colonnes)

    def index(self, ligne: int, colonne: int) -> int:
        """Convertit (ligne, colonne) en index dans la liste"""
        return (ligne - 1) * self.n_colonnes + (colonne - 1)
    
    def _dans_grille(self, ligne: int, colonne: int) -> bool:
        """Vrai si (ligne, colonne) est une case valide de la grille."""
        return 1 <= ligne <= self.n_lignes and 1 <= colonne <= self.n_colonnes
    

    # ---------- interaction avec les bateaux ----------

    def ajoute(self, bateau):
        """
        Place un bateau sur la grille en remplaçant les caractères '.' par self.bateau
        aux positions du bateau, mais uniquement si le bateau rentre entièrement
        dans la grille. Sinon, la grille est laissée inchangée.
        """
        # vérifier d'abord que toutes les cases du bateau sont dans la grille
        for (l, c) in bateau.positions:
            if not self._dans_grille(l, c):
                return  # on ne fait rien si le bateau dépasse

        # toutes les cases sont valides → on place le bateau
        for (l, c) in bateau.positions:
            i = self.index(l, c)
            self.matrice[i] = bateau.marque
    

    def afficher(self):
        """Affiche la grille proprement"""
        for i in range(self.n_lignes):
            début = i * self.n_colonnes
            fin = début + self.n_colonnes
            ligne = self.matrice[début:fin]
            print(" ".join(ligne))

    def tirer(self, x: int, y: int, touche: str = 'x'):
        """Tire sur la case (x, y). Pour l’instant : toujours raté."""
        i = self.index(x, y)
        self.matrice[i] = touche

    
    def __str__(self):
        lignes = []
        for l in range(self.n_lignes):
            début = l * self.n_colonnes
            fin = début + self.n_colonnes
            ligne = "".join(self.matrice[début:fin])
            lignes.append(ligne)
        return "\n".join(lignes)

