from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)
actions = [1 for i in range(10000)]
done = True
for step in actions:
    if done:
        state = env.reset()
    ac = step
    state, reward, done, info = env.step(ac)
    env.render()
    print(info['life'])

env.close()