from twttr import shorten

def test_code():
    assert shorten("twitter") == "twttr"
    assert shorten("kwame") == "kwm"
    assert shorten("carrot") == "crrt"
    assert shorten("ankomah") == "nkmh"
    assert shorten("Kwame") == "Kwm"
    assert shorten("Kofi, Ama") == "Kf, m"
    assert shorten("123") == "123"
