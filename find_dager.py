from action import action
from create_item import Create_item
from message import Message
from the_end import the_end


def find_dager(charlie_earth):
    action('WalkTo('+charlie_earth.name+',MysteryWorld.BlueHouseDoor)')
    action('Enter('+charlie_earth.name+',Blacksmith.Door)')
    Sword_dager=Create_item('Sword_dager','Sword','Blacksmith.Table')
    action('WalkTo('+charlie_earth.name+',Sword_dager)')
    Message('Charlie reads the spell: Abrakha Dhabra Boom.')
    action('Take('+charlie_earth.name+',Sword_dager)')
    action('EnableEffect(Spiralflame,'+Sword_dager.name+')')
    action('Exit('+charlie_earth.name+',Blacksmith.Door')
    the_end(charlie_earth)
