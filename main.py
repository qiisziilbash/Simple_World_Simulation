from Utils.simulator import *
from Utils.world_handler import *
from Utils.class_descriptions import Agents

########################################################################################################################
# simulation parameters
########################################################################################################################
runs = 20

total_population = 4
rows, cols = 10, 10

food_parameters = {
    'probability': 0.1,
    'amounts_chances': {
        2: 10,
        4: 8,
        6: 6,
        8: 4,
        10: 2,
    }
}


initial_strength = 8
max_strength = 10
reproduction_rate = .1
power = 6

# init
number_of_agent_types = len(Agents)

agents_initial_parameters = {
    Agents.AGGRESSIVE: {
        'population': round(total_population / number_of_agent_types),
        'reproduction_rate': reproduction_rate,
        'initial_strength': initial_strength,
        'max_strength': max_strength,
        'power': power,
    },
    Agents.SCAPEGOAT: {
        'population': round(total_population / number_of_agent_types),
        'reproduction_rate': reproduction_rate,
        'initial_strength': initial_strength,
        'max_strength': max_strength,
        'power': power,
    },
    Agents.DECENT: {
        'population': round(total_population / number_of_agent_types),
        'reproduction_rate': reproduction_rate,
        'initial_strength': initial_strength,
        'max_strength': max_strength,
        'power': power,
    },
    Agents.POOR: {
        'population': round(total_population / number_of_agent_types),
        'reproduction_rate': reproduction_rate,
        'initial_strength': initial_strength,
        'max_strength': max_strength,
        'power': power,
    },
}

########################################################################################################################
world = generate_world(rows, cols, agents_initial_parameters, food_parameters)

print('======================= Initial World =======================')
print_world(world)
print(world[0][3].food)
input()


for run in range(runs):
    run_the_world(world, food_parameters['probability'])

    # does not work in pycharm (only works in terminal)
    clear_screen()

    print('=========================== Day ' + str(run+1) + ' ===========================')
    print_world(world)
    input()




