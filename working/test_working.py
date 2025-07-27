from working import convert
import pytest
def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
def test_changes():
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
def test_errors():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("09:60 AM - 17:60 PM")
    with pytest.raises(ValueError):
        convert("15 AM to 17 PM")

