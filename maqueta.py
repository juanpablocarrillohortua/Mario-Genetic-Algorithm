import numpy as np
import retro

env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
obs = env.reset()

done = False
while not done:
    env.render()
    obs, reward, done, info = env.step(env.action_space.sample())  # Acciones aleatorias
env.close()

# Acciones del juego: (Izquierda, Derecha, Salto, Ninguno)
action_space = [
    [1, 0, 0, 0],  # Mover a la izquierda
    [0, 1, 0, 0],  # Mover a la derecha
    [0, 0, 1, 0],  # Saltar
    [0, 0, 0, 0],  # No hacer nada
]
# Cada cromosoma es una lista de secuencias de acciones
def generate_individual():
    return [np.random.choice(len(action_space)) for _ in range(500)]  # 500 movimientos aleatorios

def evaluate_individual(individual, env):
    obs = env.reset()
    total_reward = 0
    done = False
    step_count = 0

    while not done and step_count < len(individual):
        action_idx = individual[step_count]
        obs, reward, done, info = env.step(action_space[action_idx])
        total_reward += reward
        step_count += 1
        env.render()

    return total_reward


def select(population, fitnesses):
    total_fitness = sum(fitnesses)
    pick = np.random.uniform(0, total_fitness)
    current = 0

    for i, fitness in enumerate(fitnesses):
        current += fitness
        if current > pick:
            return population[i]

def crossover(parent1, parent2):
    point = np.random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(individual, mutation_rate=0.01):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] = np.random.choice(len(action_space))


def genetic_algorithm(env, generations=100, population_size=50):
    population = [generate_individual() for _ in range(population_size)]

    for generation in range(generations):
        fitnesses = [evaluate_individual(individual, env) for individual in population]
        new_population = []

        # Selección y cruce
        for _ in range(population_size // 2):
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)

            # Mutación
            mutate(child1)
            mutate(child2)

            new_population.append(child1)
            new_population.append(child2)

        population = new_population
        best_fitness = max(fitnesses)
        print(f"Generación {generation + 1} - Mejor fitness: {best_fitness}")


env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
genetic_algorithm(env)
env.close()

