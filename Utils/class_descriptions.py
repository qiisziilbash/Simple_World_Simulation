from enum import Enum


class Agents(Enum):
    AGGRESSIVE = ('△', '▲')
    SCAPEGOAT = ('◇', '◈')
    DECENT = ('▢', '▣')
    POOR = ('○', '◉')


class Directions(Enum):
    North  = (0, -1)
    South = (0, 1)
    East = (1, 0)
    West = (-1, 0)


class Agent:
    def __init__(self, name, strength, max_strength, initial_strength, power, position, reproduction_rate):
        self.name = name
        self.strength = strength
        self.max_strength = max_strength
        self.initial_strength = initial_strength
        self.power = power
        self.position = position
        self.reproduction_rate = reproduction_rate

    def decrease_strength(self):
        self.strength -= 1

    def give_food(self):
        self.strength += 2

    def is_alive(self):
        return self.strength > 0

    def has_open_neighbor(self, world):
        return len(self.get_open_neighbors(world)) > 0

    def get_current_reproduction_rate(self):
        return self.reproduction_rate * self.strength / self.max_strength

    def get_open_neighbors(self, world):
        directions = [direction.value for direction in Directions]
        neighbors = []
        for direction in directions:
            x = self.position[0] + direction[0]
            y = self.position[1] + direction[1]

            if 0 < x < len(world[0]) and 0 < y < len(world):
                if world[x][y].agent is not None:
                    neighbors.append(
                        tuple(
                            map(
                                lambda i, j: i + j, self.position, direction
                            )
                        )
                    )

        return neighbors

    def give_birth(self, birth_position):
        baby = Agent(self.name,
                     self.initial_strength,
                     self.max_strength,
                     self.initial_strength,
                     self.power,
                     birth_position,
                     self.reproduction_rate)
        return baby


class Cell:
    """
        food is a positive and even integer
        agent is an Agent object; if there is no agent it will be None
    """

    def __init__(self, food, agent):
        self.food = food
        self.agent = agent

    def is_open(self):
        return self.agent is None

    def has_food(self):
        return self.food > 0

    def decrease_food(self):
        if self.food > 0:
            self.food -= 2
