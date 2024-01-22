import gymnasium as gym 
import numpy as np



env = gym.make('FrozenLake-v1', map_name = "8x8", is_slippery = True, render_mode = "human")

state = env.reset()[0] # States 0 - 63, 0 -> top left, 63 -> bottom right 
terminated = False  # True when fall in hole or reached goal  
truncated = False   # True when actions > 200

while (not terminated and not truncated): 
    action = env.action_space.sample() # actions: left -> 0, down -> 1, right -> 2, up -> 3
    new_state, reward, terminated, truncated, _ = env.step(action)
    state = new_state 

env.close() 

 

