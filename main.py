from time import sleep

# simulation parameters
from Utils.world_handler import run_the_world

runs = 1000
dealy = 0.2

number_of_agents = 4
agents_with_foods = ['▲', '	▣', '◈', '◉']
agents_without_foods = ['△', '▢', '◇', '○']
total_population = 1000

rows, cols = 10, 10

# init
world = [[' ' for i in range(cols)] for j in range(rows)]
agents_initial_distribution = [total_population / 4] * number_of_agents


for run in range(runs):
    world = run_the_world(world)
    sleep(.5)
