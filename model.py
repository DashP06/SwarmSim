import mesa
import seaborn as sns
import numpy as np
import pandas as pd

from agent import BirdAgent
from mesa.experimental.continuous_space import ContinuousSpace

class BirdModel(mesa.Model):

    def __init__(
            self, 
            population_size, 
            width, 
            height, 
            speed, 
            turn_speed,
            vision,
            align_factor,
            seed=None
        ):
        super().__init__(seed=seed)
        self.num_agents = population_size
        self.space = ContinuousSpace([[0, width], [0, height]], torus=True)

        # Create agents
        agents = BirdAgent.create_agents(self, population_size, self.space, speed, turn_speed, vision, align_factor)
        # x = self.rng.random(population_size) * width # N-length array of x positions
        # y = self.rng.random(population_size) * height
        # for a, i, j in zip(agents, x, y):
        #     self.space.place_agent(a, (i, j))

    def step(self):
        """Advance the model by one step"""
        self.agents.shuffle_do("move")
        