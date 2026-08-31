import numpy as np

def cross_entropy(logits: np.ndarray, target: int) -> float:
    shifted = logits - np.max(logits)
    log_probs = shifted - np.log(np.sum(np.exp(shifted)))
    return float(-log_probs[target])

