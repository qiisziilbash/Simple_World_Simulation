import random
from enum import Enum

from multipledispatch import dispatch


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
        self.next_position = (0, 0)
        self.reproduction_rate = reproduction_rate
        self.fought = False

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

            if 0 <= x < len(world) and 0 <= y < len(world[0]):
                if world[x][y].agent is None:
                    neighbors.append(
                        tuple(
                            map(
                                lambda i, j: i + j, self.position, direction
                            )
                        )
                    )

        return neighbors

    def plan_to_move(self, world):
        if not world[self.position[0]][self.position[1]].has_food() and self.has_open_neighbor(world):
            neighbors = self.get_open_neighbors(world)
            self.next_position = random.choice(neighbors)
        else:
            self.next_position = self.position

    @dispatch()
    def move(self):
        self.position = self.next_position

    @dispatch(tuple)
    def move(self, position):
        self.position = position

    def give_birth(self, birth_position):
        baby = Agent(self.name,
                     self.initial_strength,
                     self.max_strength,
                     self.initial_strength,
                     self.power,
                     birth_position,
                     self.reproduction_rate)
        return baby

    def has_fought(self):
        return self.fought

    def wanna_defend(self):
        if self.name == Agents.AGGRESSIVE or self.name == Agents.DECENT:
            self.fought = True
            return True
        return False

    def reset_fight(self):
        self.fought = False

    def wanna_attack(self, world, position):
        if not self.has_fought():
            if self.name == Agents.AGGRESSIVE or self.name == Agents.SCAPEGOAT:
                self.fought = True
                return True
        return False


class Cell:
    def __init__(self, food, agent):
        self.food = food
        self.agent = agent

    def is_open(self):
        return self.agent is None

    def has_food(self):
        return self.food > 0

    def get_food(self):
        return self.food

    def decrease_food(self):
        if self.food > 0:
            self.food -= 2

    def increase_food(self):
        self.food += 2

    def would_agent_attack(self):
        return not (self.has_food() or self.is_open())
