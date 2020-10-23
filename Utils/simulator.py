def move_agents(agents, world):
    return agents


def run_the_world(world):
    agents = []
    for row in world:
        for cell in row:
            if cell.agent:
                agents.append(cell.agent)

    for agent in agents:
        agent.decrease_strength()
        if world[agent.position[0]][agent.position[1]].has_food():
            agent.give_food()
            world[agent.position[0]][agent.position[1]].decrease_food()

    agents = move_agents(agents, world)

    for row in world:
        for cell in row:
            cell.agent = None

    for agent in agents:
        world[agent.position[0]][agent.position[1]].agent = agent

    return world