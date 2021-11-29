from action import action
from create_item import create_item
from message import Message

def explore_city(charlie_earth,bandit1,bandit2,bandit3):
    action('WalkTo('+charlie_earth.name+',Mysteryworld.Horse)')
    action('WalkTo('+charlie_earth.name+',Mysteryworld.WestEnd)')
    action('WalkTo('+charlie_earth.name+',Mysteryworld.Fountain)')
    action('WalkTo('+charlie_earth.name+',Mysteryworld.EastEnd)')
    action('Attack('+bandit1.name+','+charlie_earth.name+',False)')
    action('Attack('+bandit2.name+','+charlie_earth.name+',False)')
    action('MoveAway('+charlie_earth.name+')')
    