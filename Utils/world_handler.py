import random

from Utils.class_descriptions import Cell, Agent


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
            elif cell.has_food():
                print('|  ' + '.' + '  ', end='')
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


def distribute_food(world, food_parameters):
    available_food_amounts = []
    for food_amount, chance in food_parameters['amounts_chances'].items():
        available_food_amounts.extend([food_amount] * chance)

    for row in world:
        for cell in row:
            if random.random() < food_parameters['probability']:
                cell.food = random.choice(available_food_amounts)


def create_agents(world, agents_parameters, rows, cols):
    agents = []
    for agent_type, properties in agents_parameters.items():
        for i in range(properties['population']):
            agents.append(Agent(agent_type,
                                properties['initial_strength'],
                                properties['max_strength'],
                                properties['initial_strength'],
                                properties['power'],
                                (0, 0),
                                properties['reproduction_rate'])
                          )

    open_positions = [(i, j) for i in range(rows) for j in range(cols)]
    chosen_positions = random.sample(open_positions, len(agents))

    for agent, position in zip(agents, chosen_positions):
        agent.position = position
        world[agent.position[0]][agent.position[1]].agent = agent


def generate_world(rows, cols, agents_parameters, food_parameters):

    world = [[Cell(0, None) for i in range(cols)] for j in range(rows)]

    create_agents(world, agents_parameters, rows, cols)

    distribute_food(world, food_parameters)

    return world
