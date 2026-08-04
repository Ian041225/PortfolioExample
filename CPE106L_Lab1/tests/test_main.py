from src.main import add

def test_one():
    assert add(2, 5) == 7

def test_two():
    assert add(-2, -8) == 10

def test_three():
    assert add(5, 0) == 5