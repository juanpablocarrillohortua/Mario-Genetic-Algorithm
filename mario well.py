import random
import time
from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)
actions = [1 for i in range(1000)]

done = True
for step in range(len(actions)):
    if done:
        state = env.reset()

    action = actions[step]
    state, reward, done, info = env.step(action)
    env.render()

env.close()