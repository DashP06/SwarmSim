import mesa
import seaborn as sns
import numpy as np
import pandas as pd
import typing

# https://mesa.readthedocs.io/stable/examples/basic/boid_flockers.html

from mesa.experimental.continuous_space import ContinuousSpaceAgent
# Vector = np.ndarray[np.float64] # 1x2 array

class BirdAgent(ContinuousSpaceAgent):

    def __init__(self, model, space, speed, turn_speed, vision, align_factor):
        super().__init__(space, model)
        self.speed = speed
        self.turn_speed = turn_speed
        self.vision = vision
        self.align_factor = align_factor
        self.direction = self.vectorize_heading(self.rng.random() * (2 * np.pi)) # Heading is any random direction. Heading of 0 is pointed right.
        self.neighbors = []

    def move(self):
        # Debug info
        # print(f"Hi, I am a bird agent. My name is {str(self.unique_id)}. My location is {str(self.pos)}.")

        # Get neighbors
        neighbors, distances = self.get_neighbors_in_radius(radius=self.vision)
        self.neighbors = [n for n in neighbors if n is not self]

        # Maintain direction
        if not neighbors:
            # Change position by moving in the direction of heading
            dpos = self.direction * self.speed
        else:
            self.direction += np.asarray([n.pos for n in self.neighbors]) * self.align_factor

        self.direction = self.direction / np.linalg.norm(self.direction)
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