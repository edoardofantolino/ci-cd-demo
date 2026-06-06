from app.calculator import add

def test_add():
    assert add(2, 3) == 7

def test_add_2():
    assert add(3, 4) == 7