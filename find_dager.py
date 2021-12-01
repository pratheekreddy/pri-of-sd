from action import action
from create_item import Create_item
from message import Message


def find_dager(charlie_earth,b_shop_vendor):
    action('WalkTo('+charlie_earth.name+',MysteryWorld.BlueHouseDoor)')
    action('Enter('+charlie_earth.name+',Blacksmith.Door)')
    Create_item('Sword','Sword','Blacksmith.Table')
    action('WalkTo('+charlie_earth.name+',Sword)')
    action('Take('+charlie_earth.name+',Sword)')
    action('WalkTo('+charlie_earth.name+', '+b_shop_vendor.name+')')
    action('Face('+b_shop_vendor.name+','+charlie_earth.name+')')
    Message('Charlie: Hi! can I get this sword please')
    Message('Vendor: Sure! Have a good day!')
    action('Exit('+charlie_earth.name+',Blacksmith.Door')
