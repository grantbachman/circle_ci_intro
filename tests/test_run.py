from app.run import multiply

def test_multiply():
    assert multiply(3, 4) == 12

def test_circle_ci_fails():
    assert False
