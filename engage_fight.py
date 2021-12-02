from MysteryWorld import MysteryWorld
from action import action

def engage_fight(charlie_earth,bandit1,bandit2,bandit3):
    action('Attack('+charlie_earth.name+','+bandit1.name+')',False)
    action('Attack('+bandit2.name+','+charlie_earth.name+')',False)
    action('Attack('+bandit3.name+','+charlie_earth.name+')')
    action('Attack('+bandit1.name+','+charlie_earth.name+')')
    action('Die('+charlie_earth.name+')')
    MysteryWorld(charlie_earth)
    

