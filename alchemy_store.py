from action import action
from Class.create_item import Create_item


def AlchemyStore(charlie_earth,a_shop_vendor):
    action('Enter('+charlie_earth.name+',AlchemyShop.Door)')
    Create_item('Apple','Apple','AlchemyShop.Table')
    Create_item('EvilBook','EvilBook','AlchemyShop.Bookshelf')
    action('WalkTo('+charlie_earth.name+',EvilBook)')
    action('Take('+charlie_earth.name+',EvilBook)')
    action('WalkTo('+charlie_earth.name+',Apple)')
    action('Take('+charlie_earth.name+',Apple)')
    action('WalkTo('+charlie_earth.name+', '+a_shop_vendor.name+')')
    action('Face('+a_shop_vendor.name+','+charlie_earth.name+')')
    action('SetNarration('+charlie_earth.name+': Hi! can I get these two items please)')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')
    action('SetNarration('+a_shop_vendor.name+': Sure! Have a good day!)')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')
    action('Exit('+charlie_earth.name+',AlchemyShop.Door')