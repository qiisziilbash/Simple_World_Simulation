import random

from Utils.class_descriptions import Cell, Agent, Agents


def print_world(world):
    for i in range(len(world[0])):
        print('======', end='')
    print('=')

    for i in range(len(world[0])):
        print('|▔▔▔▔▔', end='')
    print('|')

    row_counter = 0

    for row in world:
        for cell in row:
            if cell.agent:
                value = cell.agent.name.value[0] if cell.food == 0 else cell.agent.name.value[1]
                print('|  ' + value + '  ', end='')
            else:
                print('|     ', end='')
        print('|')
        for i in range(len(world[0])):
            print('|     ', end='')
        print('|')

        if row_counter < len(world) - 1:
            for i in range(len(world[0])):
                print('|▔▔▔▔▔', end='')
            print('|')
        else:
            for i in range(len(world[0])):
                print(' ▔▔▔▔▔', end='')
        row_counter += 1

    print('')
    for i in range(len(world[0])):
        print('======', end='')
    print('=')


def generate_world(rows, cols, agents_initial_distribution):
    """
    :return: an empty matrix of empty cells with no food
    """
    # TODO handle food distribution
    world = [[Cell(random.choice([0, 0, 0, 2, 2, 4]), None) for i in range(cols)] for j in range(rows)]

    agents = []
    for agent_type, population in agents_initial_distribution.items():
        for i in range(population):
            agents.append(Agent(agent_type, 8, 10, 2, (0, 0)))

    open_positions = [(i, j) for i in range(rows) for j in range(cols)]
    chosen_positions = random.sample(open_positions, len(agents))

    for agent, position in zip(agents, chosen_positions):
        agent.position = position
        world[agent.position[0]][agent.position[1]].agent = agent

    return world
