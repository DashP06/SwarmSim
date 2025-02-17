# App taken from https://mesa.readthedocs.io/stable/examples/basic/boid_flockers.html

import os
import sys

sys.path.insert(0, os.path.abspath("../../../.."))
from mesa.visualization import Slider, SolaraViz, make_space_component

from model import BirdModel

# starter_model = BirdModel(n=1, width=100, height=100)
# for _ in range(10):
#     starter_model.step()

def boid_draw(agent):
    return {"color": "green", "size": 20}

model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "population_size": Slider(
        label="Number of boids",
        value=100,
        min=10,
        max=200,
        step=10,
    ),
    "width": 100,
    "height": 100,
    "speed": Slider(
        label="Speed of Boids",
        value=5,
        min=1,
        max=20,
        step=1,
    ) # ,
    # "vision": Slider(
    #     label="Vision of Bird (radius)",
    #     value=10,
    #     min=1,
    #     max=50,
    #     step=1,
    # ),
    # "separation": Slider(
    #     label="Minimum Separation",
    #     value=2,
    #     min=1,
    #     max=20,
    #     step=1,
    # ),
}

model = BirdModel()

page = SolaraViz(
    model,
    components=[make_space_component(agent_portrayal=boid_draw, backend="matplotlib")],
    model_params=model_params,
    name="Bird Flocking Model",
)
page