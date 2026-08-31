def gradient_descent(a: float = 2.0, lr: float = 0.1, steps: int = 100) -> float:
    x = 0.0
    for _ in range(steps):
        grad = 2.0 * (x - a)
        x -= lr * grad
    return x

