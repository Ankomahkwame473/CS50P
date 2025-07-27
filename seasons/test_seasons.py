from seasons import convert_bdate_to_days
from datetime import date

def test_convert():
    assert convert_bdate_to_days(date(2025,7,20), date(1970,1,1)) == 20289
