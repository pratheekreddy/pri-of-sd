from action import action
from message import Message


def MysteryWorld(charlie_earth):
    action('Enter('+charlie_earth.name+',Mysteryworld.NorthEnd)',False)
    action('CreateEffect('+charlie_earth+',Resurrection)')