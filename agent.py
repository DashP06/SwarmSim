import mesa
import seaborn as sns
import numpy as np
import pandas as pd

class BirdAgent(mesa.Agent):

    def __init__(self, model):
        super().__init__(model)

    def say_hi(self):
        # The agent's step will go here.
        # For demonstration purposes we will print the agent's unique_id
        print(f"Hi, I am a bird agent. My name is {str(self.unique_id)}. My location is {str(self.pos)}.")