import random

# Кількість ітерацій генетичного алгоритму
NUM_ITERATIONS = 100

# Кількість геномів у популяції
POPULATION_SIZE = 100

# Ймовірність мутації гена
MUTATION_RATE = 0.1

# Кількість лекційних занять
NUM_LECTURES = 10

# Кількість практичних занять
NUM_PRACTICALS = 20

# Кількість викладачів
NUM_TEACHERS = 5

# Кількість студентів
NUM_STUDENTS = 50

# Кількість аудиторій
NUM_ROOMS = 5

# Розмір кожної аудиторії
ROOM_SIZE = {
    1: 15,
    2: 20,
    3: 25,
    4: 30,
    5: 35
}

# Графік, що містить інформацію про те, хто викладає, де і коли
schedule = {}

# Створення початкової популяції
def create_population():
    population = []
    for i in range(POPULATION_SIZE):
        genome = []
        for j in range(NUM_LECTURES + NUM_PRACTICALS):
            genome.append(random.randint(1, NUM_ROOMS))
        population.append(genome)
    return population

# Функція оцінки пристосованості геному
def fitness(genome):
    conflicts = 0
    schedule.clear()
    for i in range(NUM_LECTURES):
        room = genome[i]
        if ROOM_SIZE[room] < NUM_STUDENTS:
            conflicts += 1
        if room in schedule:
            conflicts += 1
        schedule[room] = i
    for i in range(NUM_PRACTICALS):
        teacher = random.randint(1, NUM_TEACHERS)
        room = genome[NUM_LECTURES + i]
        if ROOM_SIZE[room] < NUM_STUDENTS:
            conflicts += 1
        if room in schedule:
            conflicts += 1
        schedule[room] = (teacher, i)
    return conflicts

# Функція розмноження геному
def reproduce(parent1, parent2):
    midpoint = random.randint(1, len(parent1) - 1)
    child = parent1[:midpoint] + parent2[midpoint:]
    return child

# Функція мутації геному
def mutate(genome):
    for i in range(len(genome)):
        if random.random() < MUTATION_RATE:
            genome[i] = random.randint(1, NUM_ROOMS)
    return genome

# Генетичний алгоритм
def genetic_algorithm():
    population = create_population()
    best_genome = None
    for i in range(NUM_ITERATIONS):
        # Оцінка пристосованості кожного геному в популяції
        fitness_scores = [fitness(genome) for genome in population]
        # Знаходження найкращого геному в популяції
        best_genome = population[fitness_scores.index(min(fitness_scores))]
        # Створення нової популяції з найкращим геномом
        new_population = [best_genome]
        # Додавання нових геномів до популяції за допомогою розмноження та мутації
        while len(new_population) < POPULATION_SIZE:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = reproduce(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        # Заміна старої популяції на нову
        population = new_population
# Повернення найкращого геному в популяції
    return best_genome


if __name__ == "__main__":
    best_genome = genetic_algorithm()
    print("Best Genome:", best_genome)
    print("Schedule: {}".format(schedule))
    for room, data in schedule.items():
        if isinstance(data, int):
            print("Lecture {}: Room {}".format(data, room))
        else:
            teacher, practical = data
            print("Practical {}: Teacher {}, Room {}".format(practical, teacher, room))
