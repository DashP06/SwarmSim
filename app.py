# Use pygame instead of solara

# import os
# import sys

# sys.path.insert(0, os.path.abspath("../../../.."))
# from mesa.visualization import Slider, SolaraViz, make_space_component
import pygame
pygame.init()

from model import BirdModel

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()
canvas = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
canvas.fill((255, 255, 255))
font = pygame.font.SysFont("Arial" , 18 , bold = True)


starter_model = BirdModel(population_size=10, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

# Count FPS
def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    screen.blit(fps_t,(0,0))

running = True
while running:
    # Check for user pressing the X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    starter_model.step()

    # Fill screen with white
    canvas.fill((255, 255, 255)) 

    # Draw each agent to the screen
    for agent in starter_model.agents:
        x, y = agent.pos
        pygame.draw.circle(canvas, (0, 0, 0), (int(x), int(y)), 2.5)

    screen.blit(canvas, (0, 0))
    fps_counter()
    pygame.display.flip()

    # Set FPS

    clock.tick_busy_loop(60)


pygame.quit()