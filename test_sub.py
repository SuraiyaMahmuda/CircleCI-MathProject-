# test_subtraction.py
from sub import subtract

def test_subtract():
    assert subtract(10, 5) == 6
    assert subtract(20, 0) == 20
    assert subtract(0, 10) == -10
    assert subtract(-5, -5) == 0
    assert subtract(-10, 5) == -15
