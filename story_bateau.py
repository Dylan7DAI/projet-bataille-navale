# story_bateau.py
# User Story : "chevauchement"
# Utilisateur : un joueur
# Story : Positionner des bateaux sans chevauchement

from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin


def chevauchent(b1, b2) -> bool:
    """Retourne True si les deux bateaux ont au moins une case en commun."""
    # 使用集合交集来判断有没有共同的 (ligne, colonne)
    return bool(set(b1.positions) & set(b2.positions))


if __name__ == "__main__":
    # 1) 两艘重叠的例子
    b1 = Bateau(2, 3, longueur=3, vertical=False)   # 占 (2,3),(2,4),(2,5)
    b2 = Bateau(2, 4, longueur=2, vertical=True)    # 占 (2,4),(3,4) → 与 b1 在 (2,4) 重叠

    print("Bateaux b1 et b2 :")
    print("b1 positions :", b1.positions)
    print("b2 positions :", b2.positions)
    print("Chevauchent-ils ?", chevauchent(b1, b2))   # 应该是 True
    print()

    # 2) 两艘不重叠的例子
    b3 = Bateau(1, 1, longueur=2, vertical=False)     # (1,1),(1,2)
    b4 = Bateau(3, 5, longueur=3, vertical=True)      # (3,5),(4,5),(5,5)

    print("Bateaux b3 et b4 :")
    print("b3 positions :", b3.positions)
    print("b4 positions :", b4.positions)
    print("Chevauchent-ils ?", chevauchent(b3, b4))   # 应该是 False
