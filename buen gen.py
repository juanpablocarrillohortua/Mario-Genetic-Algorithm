import numpy as np
import random
from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

# env.step(action) se usa para enviar inputs
pos_brander = 3186
jump_duration = 10

class DNA:
    def __init__(self, target, mutation_rate, n_individuals, n_selection, n_generations, verbose=True):
        self.target = target
        self.mutation_rate = mutation_rate
        self.n_individuals = n_individuals
        self.n_selection = n_selection
        self.n_generations = n_generations
        self.verbose = verbose

    @staticmethod
    def create_idividual():
        actions = [0, 1, 2, 3]
        # create an individual
        individual = [random.choice(actions) for i in range(30000)]

        return individual

    def create_population(self):
        # create the population
        population = [self.create_idividual() for i in range(self.n_individuals)]

        return population

    def fitness(self, individual):
        # evaluate individual
        total_reward = 0
        done = True
        for step in individual:
            if done:
                state = env.reset()

            action = step

            if action == 2 or action == 3:
                # long jump
                for _ in range(jump_duration):
                    state, reward, done, info = env.step(action)
                    total_reward += reward
                    env.render()
                    if info['life'] < 2:
                        env.reset()
                        print(total_reward)
                        return total_reward
                    if done:
                        break
            else:
                # normal action
                state, reward, done, info = env.step(action)
                total_reward += reward
                env.render()
                if info['life'] < 2:
                    env.reset()
                    print(total_reward)
                    return total_reward


    def selection(self, population):
        scores = [(self.fitness(i), i) for i in population]
        scores = [i[1] for i in sorted(scores)]
        selected = scores[len(scores) - self.n_selection:]

        return selected

    def reproduction(self, population, selected):
        point = 0
        father = []
        for i in range(len(population)):
            point = np.random.randint(1, 299)
            father = random.sample(selected, 2)

            population[i][:point] = father[0][:point]
            population[i][point:] = father[1][point:]
        print("new population has been created")
        return population

    def mutation(self, population):

        for i in range(len(population)):
            if random.random() <= self.mutation_rate:
                point = random.randint(1, 299)
                new_value = random.randint(0, 3)

                while new_value == population[i][point]:
                    new_value = random.randint(0, 3)

                population[i][point] = new_value

        return population

    def run_genetic_algorithm(self):

        population = self.create_population()

        for i in range(self.n_generations):

            if self.verbose:
                print("_______________")
                print('GENERATION: #', i)

            selected = self.selection(population)
            population = self.reproduction(population, selected)
            population = self.mutation(population)


def main():
    target = 0
    model = DNA(target=target, mutation_rate=0.02, n_individuals=15, n_selection=5, n_generations=50, verbose=True)
    model.run_genetic_algorithm()


if __name__ == '__main__':
    main()