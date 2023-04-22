import random
import numpy as np

def normalize(X):
    """
    Функція нормалізації вхідного вектора X.
    """
    maxn = np.max(X)
    minn = np.min(X)
    an = 1.0 / (maxn - minn)
    bn = -minn / (maxn - minn)
    return (X - minn) * an + bn

def kohonen_network(X, K, num_iterations=10, learning_rate=0.3, learning_rate_decay=0.05):
    """
    Реалізація алгоритму Кохонена.
    X - масив векторів вхідних даних форми (M, N), де M - кількість зразків, а N - кількість ознак.
    K - кількість класів.
    num_iterations - кількість ітерацій навчання.
    learning_rate - коефіцієнт навчання.
    learning_rate_decay - швидкість зменшення коефіцієнта навчання з кожною ітерацією.
    """
    M, N = X.shape
    # ініціалізуємо випадковими значеннями від 0.1 до 0.3
    W = np.random.uniform(0.1, 0.3, (K, N))
    for iteration in range(num_iterations):
        for m in range(M):
            x = normalize(X[m])
            # шукаємо найближчий вектор Wk
            distances = np.linalg.norm(W - x, axis=1)
            k = np.argmin(distances)
            # корегуємо компоненти вектора Wk
            W[k] += learning_rate * (x - W[k])
        # зменшуємо коефіцієнт навчання
        learning_rate -= learning_rate_decay
    # повертаємо класи для кожного вхідного вектора
    classes = np.zeros(M)
    for m in range(M):
        x = normalize(X[m])
        distances = np.linalg.norm(W - x, axis=1)
        k = np.argmin(distances)
        classes[m] = k
    return classes


if __name__ == "__main__":
    # приклад використання
    X = np.random.uniform(0, 1, (50, 4))
    print(f"Випадкові данні: {X}")
    classes = kohonen_network(X, 5)
    print(f"Класи: {classes}")
