from ai.basics.gradient_descent.solution import gradient_descent

def test_gradient_descent():
    assert abs(gradient_descent(3.0) - 3.0) < 1e-6

