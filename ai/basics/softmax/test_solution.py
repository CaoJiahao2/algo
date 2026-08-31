import numpy as np
from ai.basics.softmax.solution import softmax

def test_softmax():
    out = softmax(np.array([[1.0, 2.0, 3.0]]))
    assert out.shape == (1, 3)
    assert np.isclose(out.sum(), 1.0)
    assert np.isclose(out[0, 2], 0.66524096)

def test_softmax_stability():
    out = softmax(np.array([1000.0, 1000.0]))
    assert np.allclose(out, [0.5, 0.5])

