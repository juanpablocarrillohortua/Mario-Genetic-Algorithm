import gym_super_mario_bros
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

state = env.reset()
env.render()  # Esto debería abrir una ventana
done = False

while not done:
    action = env.action_space.sample()  # Toma una acción aleatoria
    state, reward, done, info = env.step(action)
    env.render()  # Debe seguir renderizando hasta que done sea True

env.close()  # Cierra el entorno al fin