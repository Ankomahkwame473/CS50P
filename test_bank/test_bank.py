from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("HellO") == 0
    assert value("Hello, Kwame") == 0
def test_kwame():
    assert value("kwame") == 100
def test_number():
    assert value("123") == 100
def test_char():
    assert value(".,;") == 100
def test_hey():
    assert value("hey") == 20


