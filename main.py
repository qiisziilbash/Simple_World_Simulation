from time import sleep

from Utils.simulator import run_the_world
from Utils.world_handler import generate_world, print_world, fill_random_world
from Utils.class_descriptions import Agents


# simulation parameters
runs = 1
dealy = 0.2

total_population = 1000
rows, cols = 10, 10

# init
world = generate_world(rows, cols)
world = fill_random_world(world)

agents_initial_distribution = [total_population / 4] * Agents.__len__()

print_world(world)
for run in range(runs):
    world = run_the_world(world)
    print_world(world)
    sleep(.5)
