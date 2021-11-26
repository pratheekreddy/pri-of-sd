from action import action
from create_item import create_item


def AlchemyStore(charlie_earth,a_shop_vendor):
    action('Enter('+charlie_earth.name+',AlchemyShop.Door)')
    create_item('Apple','Apple','AlchemyShop.Table')
    create_item('EvilBook','EvilBook','AlchemyShop.Bookshelf')
    action('WalkTo('+charlie_earth+',EvilBook)')
    action('Take('+charlie_earth+',EvilBook)')
    action('WalkTo('+charlie_earth+',Apple)')
    action('Take('+charlie_earth+',Apple)')
    action('WalkTo('+charlie_earth+', '+a_shop_vendor+')')
    action('Face('+a_shop_vendor+','+charlie_earth+')')
    action('SetNarration('+charlie_earth.name+': Hi! can I get these two items please)')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')
    action('SetNarration('+a_shop_vendor.name+': Sure! Have a good day!)')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')
    action('Exit('+charlie_earth+',AlchemyShop.Door')