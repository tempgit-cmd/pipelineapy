from app import check_even_odd

def test_even_number():
    assert check_even_odd(4) == "Even"

def test_odd_number():
    assert check_even_odd(5) == "Odd"

