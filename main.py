from time import sleep

from Utils.simulator import run_the_world
from Utils.world_handler import generate_world, print_world, fill_random_world
from Utils.class_descriptions import Agents


# simulation parameters
runs = 1
dealy = 0.2

total_population = 12
rows, cols = 10, 10

# init
number_of_agent_types = len(Agents)

agents_initial_distribution = {
    Agents.AGGRESSIVE: round(total_population / number_of_agent_types),
    Agents.SCAPEGOAT: round(total_population / number_of_agent_types),
    Agents.DECENT: round(total_population / number_of_agent_types),
    Agents.POOR: round(total_population / number_of_agent_types),
}

world = generate_world(rows, cols, agents_initial_distribution)


print_world(world)
for run in range(runs):
    world = run_the_world(world)
    print_world(world)
    sleep(.5)
