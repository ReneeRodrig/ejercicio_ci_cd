from src.main import multiply, to_upper, to_lower

def test_multiply():
    assert multiply(2,3) == 6
    assert multiply(0,4) == 0
    
def test_to_upper():
    assert to_upper('Renee') == 'RENEE'
    
def test_to_lower():
    assert to_lower('Renee') == 'renee'