import random


def feed_agents(agents, world):
    for agent in agents:
        agent.decrease_strength()
        if world[agent.position[0]][agent.position[1]].has_food():
            agent.give_food()
            world[agent.position[0]][agent.position[1]].decrease_food()

    return agents


def handle_encounters(agents, world):
    pass


def move_agents(agents, world):
    for agent in agents:
        if not world[agent.position[0]][agent.position[1]].has_food():
            pass

    return agents


def kill_weak_agents(agents):
    survived_agents = []
    for agent in agents:
        if agent.is_alive():
            survived_agents.append(agent)
    return survived_agents


def reproduce_strong_agents(agents, world):
    new_population = []
    for agent in agents:
        new_population.append(agent)

        if random.random() < agent.get_current_reproduction_rate() and agent.has_open_neighbor(world):
            birth_position = random.choice(agent.get_open_neighbors(world))
            baby = agent.give_birth(birth_position)
            new_population.append(baby)

    return new_population


def reproduce_food(world, food_probability):
    for row in world:
        for cell in row:
            if random.random() < food_probability:
                cell.increase_food()


def run_the_world(world, food_probability):

    agents = []
    for row in world:
        for cell in row:
            if cell.agent:
                agents.append(cell.agent)

    agents = feed_agents(agents, world)

    reproduce_food(world, food_probability)

    agents = kill_weak_agents(agents)

    agents = reproduce_strong_agents(agents, world)

    # TODO
    agents = move_agents(agents, world)

    # update population
    for row in world:
        for cell in row:
            cell.agent = None

    for agent in agents:
        world[agent.position[0]][agent.position[1]].agent = agent

