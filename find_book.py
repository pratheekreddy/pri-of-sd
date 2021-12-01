from action import action
from create_item import Create_item
from message import Message


def find_dager(charlie_earth,a_shop_vendor):
    action('Enter('+charlie_earth.name+',AlchemyShop.Door)')
    Create_item('Apple','Apple','AlchemyShop.Table')
    Create_item('EvilBook','EvilBook','AlchemyShop.Bookshelf')
    action('WalkTo('+charlie_earth.name+',Apple)')
    action('Take('+charlie_earth.name+',Apple)')
    action('WalkTo('+charlie_earth.name+',EvilBook)')
    action('Take('+charlie_earth.name+',EvilBook)')
    action('WalkTo('+charlie_earth.name+', '+a_shop_vendor.name+')')
    action('Face('+a_shop_vendor.name+','+charlie_earth.name+')')
    Message('Charlie: Hi! can I get these two items please')
    Message('Vendor: Sure! Have a good day!')
    action('Exit('+charlie_earth.name+',AlchemyShop.Door')
