import numpy as np
import random
from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

# env.step(action) se usa para enviar inputs
pos_brander = 3186


class DNA:
    def __init__(self, target, mutation_rate, n_individuals, n_selection, n_generations, verbose=True):
        self.target = target
        self.mutation_rate = mutation_rate
        self.n_individuals = n_individuals
        self.n_selection = n_selection
        self.n_generations = n_generations

    def create_idividual(self, actions=[0, 1, 2, 3]):
        # create an individual
        individual = [random.choice(actions) for i in range(300)]

        return individual

    def create_population(self):
        # create the population
        population = [self.create_idividual() for i in range(self.n_individuals)]

        return population

    def fitness(self, population):
        # evaluate individual
        for individual in population:
            done = True
            for step in range(len(individual)):
                if done:
                    state = env.reset()

                action = individual[step]
                state, reward, done, info = env.step(action)
                env.render()


def main():
    target = 0
    model = DNA(target=target, mutation_rate=0.02, n_individuals=15, n_selection=5, n_generations=50, verbose=False)
    model.fitness(model.create_population())


if __name__ == '__main__':
    main()
