from um import count

def test_words():
    assert count("Yummy") == 0
    assert count("Um?") == 1
def test_sentence():
    assert count("Um, I have um, a phone") == 2
def test_both():
    assert count("This um, food is yummy") == 1
