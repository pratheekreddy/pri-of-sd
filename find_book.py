from action import action
from create_item import Create_item
from message import Message


def find_book(charlie_earth,a_shop_vendor):
    action('Enter('+charlie_earth.name+',AlchemyShop.Door)')
    Apple_Book=Create_item('Apple_Book','Apple','AlchemyShop.Table')
    EvilBook2=Create_item('EvilBook2','EvilBook','AlchemyShop.Bookshelf')
    action('WalkTo('+charlie_earth.name+',Apple_Book)')
    action('Take('+charlie_earth.name+',Apple_Book)')
    action('WalkTo('+charlie_earth.name+',EvilBook2)')
    action('Take('+charlie_earth.name+',EvilBook2)')
    action('WalkTo('+charlie_earth.name+', '+a_shop_vendor.name+')')
    action('Face('+a_shop_vendor.name+','+charlie_earth.name+')')
    Message('Charlie: Hi! can I get these two items please')
    Message('Vendor: Sure! Have a good day!')
    action('Exit('+charlie_earth.name+',AlchemyShop.Door')
