# Simple World

## World
- an n*m matrix (borders of the matrix is blocked)
- each cell can be empty, contain a food, or a food and an agent
- each food has an amount that is a positive even integer number  
    - initially each cell has food with a specific probability   
    - amount of each food is decreased by 2 if an agent is on it and the agent hasn't reached their max strength

## Agents
- have strength
    - strength is an integer number with default value and a maximum value
    - every day agents loose one strength
    - if agents have food they gain 2 extra strength every day 
    - agents die if their strength is 0
    
- have power
    - power is a fixed integer number
    
- have a max reproduction rate
    - agents reproduction rate = max_reproduction_rate * current_strength / max_strength
    - every day agents reproduce with their reproduction rate if they have at least one open neighbor cell

    
## Rules
- agents take actions constantly unless they have food and no one is attacking or they cannot move because they are blocked
    - agents either move forward, left, right, backward if not blocked
    - each of their action has an equal probability 
    - agents can not go to the blocked cells

- if two more than one agent wants to move a specific open cell, only one of them randomly will go there and others will stay where they are
- agents encounter each other if they can reach each other in the next move and only one of them has food

- when agents encounter each other:
    - attack
        - one of the attackers get to be on the food and swap their place with the current person on the food
            - the winner is determined probabilistically and each agent's winning probability is their power over the sum of defender and all attackers' powers 
            - rest of agents stay where they are
        - if there are more than one cell to attack:
            - each agent will attack only one cell at a time
            - candidate cell's chance to be attacked is cell's food / (number of attackers + 1 defender)
    - do nothing

- there are 4 types of agents:
   - ('△') aggressive: they defend their food and fight for new food
   - ('◇') scapegoat: they do not defend their food but fight for new food
   - ('▢') decent: they do defend their food but do not fight for new food   
   - ('○') poor: they do not defend their food and do not fight for new food
 