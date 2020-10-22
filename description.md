# Simple World

## World
- an n*m matrix (borders of the matrix is blocked)
- each cell can be empty, contain a food, or a food and an agent
- each food has an amount that is a positive even integer number    
    - amount of each food is decreased by 2 if an agent is on it and hasn't reached their max strength

## Agents
- have strength
    - strength is an integer number with default value and a maximum value
    - every day agents loose one strength
    - if agents have food they gain 2 extra strength every day 
    
- have power
    - power is a fixed integer number
    
## Rules
- agents take actions constantly unless they have food and no one is attacking
    - agents either stay where they are or move forward, left, right, backward
    - each of their action has an equal probability 
    - agents can not go to the blocked cells

- agents encounter each other if they can reach each other in the next move

- when agents encounter each other:
    - attack
        - if they both attack their wining probability is power of each over the sum of their powers
        - if only one of them attacks, the attacker wins
        - if there is an attack, agents positions should be swapped if winner is not already on food
    - do nothing

- there are 4 types of agents:
   - aggressive: they defend their food and fight for new food
   - scapegoat: they do not defend their food but fight for new food
   - decent: they do defend their food but do not fight for new food   
 