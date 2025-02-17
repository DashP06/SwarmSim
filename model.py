import mesa
import seaborn as sns
import numpy as np
import pandas as pd

from agent import BirdAgent

class BirdModel(mesa.Model):

    def __init__(self, n, width, height, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        self.space = mesa.space.ContinuousSpace(width, height, torus=True)

        # Create agents
        agents = BirdAgent.create_agents(model=self, n=n)
        x = self.rng.random(n) * width # N-length array of x positions
        y = self.rng.random(n) * height
        for a, i, j in zip(agents, x, y):
            self.space.place_agent(a, (i, j))

    def step(self):
        """Advance the model by one step"""
        self.agents.shuffle_do("say_hi")

    