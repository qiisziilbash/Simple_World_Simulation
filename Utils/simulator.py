import random


def move_agents(agents, world):
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


def reproduce_food(world):
    return world


def run_the_world(world):
    # take all the agents
    agents = []
    for row in world:
        for cell in row:
            if cell.agent:
                agents.append(cell.agent)

    # handle their strength and food
    for agent in agents:
        agent.decrease_strength()
        if world[agent.position[0]][agent.position[1]].has_food():
            agent.give_food()
            world[agent.position[0]][agent.position[1]].decrease_food()

    # kill the weak agents
    agents = kill_weak_agents(agents)

    # reproduce the strong agents
    agents = reproduce_strong_agents(agents, world)

    # TODO move agents
    agents = move_agents(agents, world)

    # clean up old agents
    for row in world:
        for cell in row:
            cell.agent = None

    # add the new agents
    for agent in agents:
        world[agent.position[0]][agent.position[1]].agent = agent

    # TODO reproduce food
    world = reproduce_food(world)

    return world