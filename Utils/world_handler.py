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


def generate_world(rows, cols):
    """
    :return: an empty matrix of empty cells with no food
    """
    return [[Cell(0) for i in range(cols)] for j in range(rows)]


def fill_random_world(world):
    world[0][1] = Cell(2, Agent(Agents.AGGRESSIVE, 8, 10, 2))
    world[5][6] = Cell(0, Agent(Agents.DECENT, 8, 10, 2))
    world[3][1] = Cell(0, Agent(Agents.POOR, 8, 10, 2))
    world[9][6] = Cell(2, Agent(Agents.SCAPEGOAT, 8, 10, 2))
    return world


