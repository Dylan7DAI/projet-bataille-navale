# test_grille.py

from grille import Grille

def test_init():
    g = Grille(5, 8)
    # 长度 = 5*8
    assert len(g.matrice) == 5 * 8
    # 全部都是空字符 '.'
    assert all(case == g.vide for case in g.matrice)

def test_tirer():
    g = Grille(5, 8)
    g.tirer(2, 3)  # 在第2行第3列开火
    idx = g.index(2, 3)
    assert g.matrice[idx] == g.tir


def test_affichage_apres_tir():
    g = Grille(3, 4)
    g.tirer(2, 3)
    attendu = "....\n..x.\n...."
    assert str(g) == attendu
