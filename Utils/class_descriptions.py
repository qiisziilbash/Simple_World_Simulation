from enum import Enum


class Agents(Enum):
    AGGRESSIVE = ('△', '▲')
    SCAPEGOAT = ('◇', '◈')
    DECENT = ('▢', '▣')
    POOR = ('○', '◉')


class Agent:
    def __init__(self, name, strength, max_strength, power, position=(0, 0)):
        self.name = name
        self.strength = strength
        self.max_strength = max_strength
        self.power = power
        self.position = position

    def decrease_strength(self):
        self.strength -= 1

    def give_food(self):
        self.strength += 2

    def is_alive(self):
        return self.strength > 0


class Cell:
    """
        food is a positive and even integer
        agent is an Agent object; if there is no agent it will be None
    """

    def __init__(self, food, agent=None):
        self.food = food
        self.agent = agent

    def is_open(self):
        return self.agent is None

    def has_food(self):
        return self.food > 0

    def decrease_food(self):
        if self.food > 0:
            self.food -= 2
