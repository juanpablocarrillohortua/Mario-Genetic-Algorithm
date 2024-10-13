import random
import time
from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)
actions = [2 for i in range(10)]
jump_duration = 10

def fitness(individual):
    # evaluate individual
    total_reward = 0
    done = True
    for step in range(len(individual)):
        if done:
            state = env.reset()

        action = individual[step]

        if action == 2 or action == 3:
            # Mantener el botón de salto por varios pasos para un salto más alto
            for _ in range(jump_duration):
                state, reward, done, info = env.step(action)
                total_reward += reward
                env.render()
                time.sleep(1/60)
                if done:
                    break
        else:
            # Para otras acciones, ejecutarlas normalmente
            state, reward, done, info = env.step(action)
            total_reward += reward
            env.render()
            time.sleep(1/60)

    return total_reward

fitness(actions)