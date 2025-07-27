from plates import is_valid
def test_plate1():
    assert is_valid("CS50") == True
    assert is_valid("CS") == True
    assert is_valid("C5") == False
    assert is_valid("5C") == False
    assert is_valid("55") == False
    assert is_valid(" 5") == False
def test_plate2():
    assert is_valid("AD10") == True
    assert is_valid("AD01") == False
def test_plate3():
    assert is_valid("22CDF") == False
    assert is_valid("A2CDF") == False
    assert is_valid("2ACDF") == False
def test_plate4():
    assert is_valid("KWAMEANKOMAH") == False
    assert is_valid("KWAME") == True
    assert is_valid("KWA2ME") == False
def test_plate5():
    assert is_valid("KWAME5") == True
def test_plate6():
    assert is_valid("AA20") == True
    assert is_valid("AA20?") == False
    assert is_valid("AA?20") == False
    assert is_valid("AA20.") == False
