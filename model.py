import mesa
import seaborn as sns
import numpy as np
import pandas as pd

from agent import BirdAgent

class BirdModel(mesa.Model):

    def __init__(self, n, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        BirdAgent.create_agents(model=self, n=n)

    def step(self):
        """Advance the model by one step"""
        self.agents.shuffle_do("say_hi")