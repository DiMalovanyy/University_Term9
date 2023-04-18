import random
from typing import Any, Literal
import numpy as np
from numpy._typing import NDArray

def gen() -> list:
    class_fst: list = []
    class_snd: list = []
    for i in range(100):
        x_coord: float = random.uniform(0, 1)
        class_fst.append([np.array([x_coord,
                                    random.uniform(x_coord + 0.001, 1),
                                    random.uniform(0, 1)
                                   ]), 
                          -1])
        x_coord: float = random.uniform(0, 0.5)
        class_snd.append([np.array([x_coord,
                                    random.uniform(0, x_coord - 0.001),
                                    random.uniform(0, 1)
                                   ]),
                           1])
    return class_fst + class_snd

if __name__ == '__main__':
    alpha: float= 0.05
    points: list = gen()
    weights: NDArray[Any] = np.array([random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)])
    print(weights)
    wrong_counter = 0
    correct_counter = 0

    for point, marker in points:
        dot_sign: Any = np.sign(np.array(point).dot(weights))
        if dot_sign * marker < 0:
            wrong_counter += 1
        else:
            correct_counter += 1

    print(f"Wrong class: {wrong_counter}\nCorrect class: {correct_counter}")
    for i in range(1000):
        for point, marker in points:
            dot_sign = np.sign(np.array(point).dot(weights))
            if dot_sign * marker < 0:
                weights: NDArray[Any] = weights + alpha * marker * point
    print(weights)


    wrong_counter = 0
    correct_counter = 0

    for point, class_marker in points:
        dot_sign = np.sign(np.array(point).dot(weights))
        if dot_sign * class_marker < 0:
            wrong_counter += 1
        else:
            correct_counter += 1

    print(f"Wrong class: {wrong_counter}\nCorrect class: {correct_counter}")
