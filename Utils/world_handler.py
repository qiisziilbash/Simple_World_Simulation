
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
            print('|  ' + cell + '  ', end='')
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


def generate_random_world(world):
    world[0][1] = '*'
    world[5][6] = '◈'
    world[3][1] = '▣'
    world[9][6] = '◉'
    return world


def run_the_world(world):
    return world
