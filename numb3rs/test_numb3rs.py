from numb3rs import validate

def test_numbers():
    assert validate("123.123.123.123") == True
    assert validate("255.123.123.260") == False
def test_alphabets():
    assert validate("cat") == False
    assert validate("255.dog.123.260") == False
