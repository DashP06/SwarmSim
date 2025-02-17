import mesa
import seaborn as sns
import numpy as np
import pandas as pd

from agent import BirdAgent

class BirdModel(mesa.Model):

    def __init__(
            self, 
            population_size=100, 
            width=100, 
            height=100, 
            speed=1, 
            turn_speed=1,
            seed=None
        ):
        super().__init__(seed=seed)
        self.num_agents = population_size
        self.space = mesa.space.ContinuousSpace(width, height, torus=True)

        # Create agents
        agents = BirdAgent.create_agents(self, population_size, speed, turn_speed)
        x = self.rng.random(population_size) * width # N-length array of x positions
        y = self.rng.random(population_size) * height
        for a, i, j in zip(agents, x, y):
            self.space.place_agent(a, (i, j))

    def step(self):
        """Advance the model by one step"""
        self.agents.shuffle_do("say_hi")
        