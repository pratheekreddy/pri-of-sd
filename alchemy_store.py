from MysteryWorld import MysteryWorld
from action import action
from create_item import Create_item
from message import Message
from start import a_shop_vendor
from begining import home

def AlchemyStore(charlie_earth):
    action('Enter('+charlie_earth.name+',AlchemyShop.Door)')
    Apple=Create_item('Apple','Apple','AlchemyShop.Table')
    EvilBook=Create_item('EvilBook','EvilBook','AlchemyShop.Bookshelf')
    Bag=Create_item('Bag','Bag','AlchemyShop.Bar')
    action('EnableIcon(buy_apple,apple,Charlie,"Buy apple")')
    action('EnableIcon(buy_bag,lockedchest,Charlie,"Buy Bag")')
    action('EnableIcon(buy_book,evilbook,Charlie,"Buy Book")')
    action('EnableInput()')
    choice3(charlie_earth)
    action('DisableInput()')
    
    
def buy_apple(charlie_earth):
    action('WalkTo('+charlie_earth.name+',Apple)')
    action('Take('+charlie_earth.name+',Apple)')
    action('WalkTo('+charlie_earth.name+', '+a_shop_vendor.name+')')
    action('Face('+a_shop_vendor.name+','+charlie_earth.name+')')
    Message('Charlie: Hi! can I get this apple')
    Message('Vendor: Sure! Have a good day!')
    action('Exit('+charlie_earth.name+',AlchemyShop.Door)')
    Message('Charlie goes back home after buying an apple and another boring day starts again!')
    action('SetPosition('+charlie_earth.name+',Cottage.Bed)')
    home(charlie_earth)

def buy_bag(charlie_earth):
    action('WalkTo('+charlie_earth.name+',Bag)')
    action('Take('+charlie_earth.name+',Bag)')
    action('WalkTo('+charlie_earth.name+', '+a_shop_vendor.name+')')
    action('Face('+a_shop_vendor.name+','+charlie_earth.name+')')
    Message('Charlie: Hi! can I get these this bag')
    Message('Vendor: Sure! Have a good day!')
    action('Exit('+charlie_earth.name+',AlchemyShop.Door)')
    Message('Charlie goes back home after buying a bag and another boring day starts again!')
    action('SetPosition('+charlie_earth.name+',Cottage.Bed)')
    home(charlie_earth)

def buy_book(charlie_earth):
    action('WalkTo('+charlie_earth.name+',EvilBook)')
    action('Take('+charlie_earth.name+',EvilBook)')
    action('WalkTo('+charlie_earth.name+', '+a_shop_vendor.name+')')
    action('Face('+a_shop_vendor.name+','+charlie_earth.name+')')
    Message('Charlie: Hi! can I get these two items please')
    Message('Vendor: Sure! Have a good day!')
    action('Exit('+charlie_earth.name+',AlchemyShop.Door)')
    charlie_earth.item='book'
    Message('Oh boy! You picked an "Evil book" so now you will be summoned to the mystery world!')
    MysteryWorld(charlie_earth)

def choice3(charlie_earth):
    while True:
        received=input()
        if received=='input buy_apple Charlie':
           return buy_apple(charlie_earth)
        elif received=='input buy_bag Charlie':
           return buy_bag(charlie_earth)
        elif received=='input buy_book Charlie':
            return buy_book(charlie_earth)