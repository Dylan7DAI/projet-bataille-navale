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
