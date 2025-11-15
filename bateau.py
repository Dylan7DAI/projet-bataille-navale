# bateau.py

class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
        self.marque = '⛵'

    @property
    def positions(self):
        pos = []
        for i in range(self.longueur):
            if self.vertical:
                pos.append((self.ligne + i, self.colonne))
            else:
                pos.append((self.ligne, self.colonne + i))
        return pos

    def coule(self, grille) -> bool:
        """Retourne True si toutes les cases du bateau sont marquées 'x' sur la grille."""
        for (l, c) in self.positions:
            i = grille.index(l, c)
            symbole = grille.matrice[i]
            if symbole != grille.tir and symbole != self.marque:   
                return False
        return True
    

class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical)
        self.marque = "🚢"   


class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical)
        self.marque = "⛴"


class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "🚣"


class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "🐟"
