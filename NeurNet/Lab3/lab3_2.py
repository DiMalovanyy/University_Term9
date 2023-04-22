import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt


def kohonen_map(X, M, max_time=100, learning_rate=0.1, initial_radius=1.0, 
                time_constant=10.0):
    """
    Навчання мережі Кохонена на вхідних даних X з M нейронами.
    
    Параметри:
        X: numpy.ndarray, вхідні дані розміру (num_samples, num_features).
        M: int, кількість нейронів у мережі.
        max_time: int, максимальний час для навчання.
        learning_rate: float, коефіцієнт навчання η₀.
        initial_radius: float, початковий радіус σ₀.
        time_constant: float, константа часу для експоненційного зменшення
            радіуса σ(t) і коефіцієнта навчання η(t).
    
    Повертає:
        W: numpy.ndarray, матриця вагів розміру (M, num_features),
            що містить вектора Wm для кожного нейрона.
    """
    num_samples, num_features = X.shape
    # Ініціалізуємо матрицю вагів випадковими числами.
    W = np.random.rand(M, num_features) * X.max()
    # Початковий час.
    t = 1
    while t <= max_time:
        # Вибираємо випадковий вхідний вектор.
        x = X[np.random.choice(num_samples)]
        # Знаходимо нейрон, який найближчий до вектора x.
        distances = np.linalg.norm(W - x, axis=1)
        closest_neuron_index = np.argmin(distances)
        # Обчислюємо параметри навчання.
        learning_rate_t = learning_rate * np.exp(-t / time_constant)
        radius_t = initial_radius * np.exp(-t / time_constant)
        # Оновлюємо ваги всіх нейронів.
        for i in range(M):
            distance_to_winner = np.linalg.norm(i - closest_neuron_index)
            h = np.exp(-(distance_to_winner ** 2) / (2 * radius_t ** 2))
            W[i] += learning_rate_t * h * (x - W[i])
        # Збільшуємо час на одиницю.
        t += 1
    return W


# Функція для вибору найближчого нейрона.
def find_closest_neuron(x, W):
    distances = np.linalg.norm(W - x, axis=1)
    closest_neuron_index = np.argmin(distances)
    return closest_neuron_index

if __name__ == "__main__":
    # Згенеруємо випадкові дані.
    num_samples = 1000
    num_features = 2
    X = np.random.rand(num_samples, num_features)

    # Задамо параметри для мережі Кохонена.
    M = 25
    max_time = 100
    learning_rate = 0.1
    initial_radius = 1.0
    time_constant = 10.0

    # Навчаємо мережу Кохонена на випадкових даних.
    W = kohonen_map(X, M, max_time, learning_rate, initial_radius, time_constant)

    # Накладаємо еталонні значення на карту.
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(W[:, 0], W[:, 1], color='b')

    for i in range(num_samples):
        x = X[i]
        distances = np.linalg.norm(W - x, axis=1)
        closest_neuron_index = np.argmin(distances)
        ax.scatter(W[closest_neuron_index, 0], W[closest_neuron_index, 1], color='r')

    ax.set_title('Карта Кохонена з еталонними значеннями')
    ax.set_xlabel('Ось X')
    ax.set_ylabel('Ось Y')

    plt.show()

    # Визначаємо найближчий нейрон для вектора X.
    X_test = np.array([0.4, 0.6])
    distances = np.linalg.norm(W - X_test, axis=1)
    closest_neuron_index = np.argmin(distances)

    # Відображаємо результат на карті Кохонена.
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(W[:, 0], W[:, 1], color='b')
    ax.scatter(W[closest_neuron_index, 0], W[closest_neuron_index, 1], color='r')
    ax.set_title('Карта Кохонена з відображеним найближчим нейроном')
    ax.set_xlabel('Ось X')
    ax.set_ylabel('Ось Y')

    plt.show()
