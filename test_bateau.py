from grille import Grille
from bateau import Bateau

def test_bateau_default():
    b = Bateau(2, 3)
    assert b.ligne == 2
    assert b.colonne == 3
    assert b.longueur == 1
    assert b.vertical == False

def test_positions_horizontal():
    b = Bateau(2, 3, longueur=3)
    assert b.positions == [(2,3), (2,4), (2,5)]

def test_positions_vertical():
    b = Bateau(2, 3, longueur=3, vertical=True)
    assert b.positions == [(2,3), (3,3), (4,3)]




def test_bateau_coule():
    g = Grille(3, 3)
    b = Bateau(2, 2, longueur=2)
    g.ajoute(b)

    # 还没被打 → 不沉
    assert b.coule(g) is False

    # 打中一个格子 → 还没沉
    g.tirer(2, 2)
    assert b.coule(g) is False

    # 打中所有格子 → 船沉
    g.tirer(2, 3)
    assert b.coule(g) is True



from bateau import PorteAvion, Croiseur

def test_porte_avion_longueur_et_marque():
    b = PorteAvion(1, 1)
    assert b.longueur == 4
    assert b.marque == "🚢"

def test_ajoute_type_bateau_sur_grille():
    g = Grille(2, 4)
    b = PorteAvion(1, 1, vertical=False)
    g.ajoute(b)

    # Porte-avion 占 (1,1),(1,2),(1,3),(1,4)
    for col in range(1, 5):
        idx = g.index(1, col)
        assert g.matrice[idx] == b.marque
