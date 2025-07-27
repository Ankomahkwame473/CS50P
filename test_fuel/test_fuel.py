import fuel
import pytest

def test_convert():
    assert fuel.convert("1/2") == 50
    assert fuel.convert("1/4") == 25
def test_error():
    with pytest.raises(ValueError):
        fuel.convert("X/2")
    with pytest.raises(ValueError):
        fuel.convert("-1/2")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")
def test_gauge():
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
