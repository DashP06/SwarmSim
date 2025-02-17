import mesa
import seaborn as sns
import numpy as np
import pandas as pd
import typing

# Vector = np.ndarray[np.float64] # 1x2 array

class BirdAgent(mesa.Agent):

    def __init__(self, model, speed, turn_speed):
        super().__init__(model)
        self.speed = speed
        self.turn_speed = turn_speed
        self.heading = self.rng.random() * (2 * np.pi) # Heading is any random direction. Heading of 0 is pointed right.

    def say_hi(self):
        # The agent's step will go here.
        # For demonstration purposes we will print the agent's unique_id
        # print(f"Hi, I am a bird agent. My name is {str(self.unique_id)}. My location is {str(self.pos)}.")

        # Delta Position: Tuple (x, y) | -speed <= x, y < speed (if speed == 1.0, -1.0 <= x, y < 1.0)
        # dpos = ((2 * self.speed) * self.rng.random(2) - self.speed) 

        # Change position by moving in the direction of heading
        dpos = self.vectorize_heading(self.heading) * self.speed
        self.pos = self.model.space.torus_adj(self.pos + dpos) # Move by dpos, and handle torus wrapping 

    # In pygame (0, 0) is the top left corner. Positive X points right and positive Y points down. 
    # Takes a float heading, returns a unit 2-vector
    @staticmethod
    def vectorize_heading(heading):
        return np.array([np.cos(heading), np.sin(heading)])
    
    # Takes a 2-vector, returns a float
    @staticmethod
    def heading_from_vector(vector):
        return np.atan2(*vector)