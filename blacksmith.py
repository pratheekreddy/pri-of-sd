from MysteryWorld import MysteryWorld
from action import action
from create_item import Create_item
from message import Message
from start import b_shop_vendor

def BlackSmith(charlie_earth):
    action('Enter('+charlie_earth.name+',Blacksmith.Door)')
    Sword_b=Create_item('Sword_b','Sword','Blacksmith.Table')
    action('WalkTo('+charlie_earth.name+',Sword_b)')
    action('Take('+charlie_earth.name+',Sword_b)')
    charlie_earth.item='dagger'
    action('WalkTo('+charlie_earth.name+', '+b_shop_vendor.name+')')
    action('Face('+b_shop_vendor.name+','+charlie_earth.name+')')
    Message('Charlie: Hi! can I get this sword please')
    Message('Vendor: Sure! Have a good day!')
    action('Exit('+charlie_earth.name+',Blacksmith.Door')
    MysteryWorld(charlie_earth)