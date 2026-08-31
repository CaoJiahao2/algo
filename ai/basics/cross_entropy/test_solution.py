import numpy as np
from ai.basics.cross_entropy.solution import cross_entropy

def test_cross_entropy():
    loss = cross_entropy(np.array([1.0, 2.0, 3.0]), 2)
    assert np.isclose(loss, 0.40760596)

