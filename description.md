# Simple World

## World
- An n*m matrix (borders of the matrix is blocked)
- each cell can be empty, contain a food, or a food and an agent
- each food has an amount that is a positive even integer number    
    - amount of each food is decreased by 2 if an agent is on it and hasn't reached their max strength

## Agents
- have strength
    - strength is an integer number with default value and a maximum value
    - every day agents loose one strength
    - if agents have food they gain 2 strength every day 
    
- have power
    - power is a fixed integer number

# aggressive defend their resource and fight for new resources
# scape_goat does not defend their resources but fight for new resources
# decent defend their resources and does not fight for new resources
# poor does not defend their resources and does not fight for new resources

# all of them wander if they don't have resources (with equal probability to left, right, or straight if not blocked)
# encounter happens when two agents are next to each other (8 cell neighborhood)
# when encounter happens agents can choose attack or do nothing
#  >> if only one attacks they get the food and the other should leave
#  >> if both attack winner is 50/50