import mesa
import seaborn as sns
import numpy as np
import pandas as pd

class BirdAgent(mesa.Agent):

    def __init__(self, model):
        super().__init__(model)
        self.birdspeed = 10

    def say_hi(self):
        # The agent's step will go here.
        # For demonstration purposes we will print the agent's unique_id
        print(f"Hi, I am a bird agent. My name is {str(self.unique_id)}. My location is {str(self.pos)}.")

        # Delta Position: Tuple (x, y) | -birdspeed <= x, y < birdspeed (if birdspeed == 1.0, -1.0 <= x, y < 1.0)
        dpos = ((2 * self.birdspeed) * self.rng.random(2) - self.birdspeed) 
        self.pos = self.model.space.torus_adj(self.pos + dpos) # Move by dpos, and handle torus wrapping 
