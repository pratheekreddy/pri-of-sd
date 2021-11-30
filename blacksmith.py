from action import action
from Class.create_item import Create_item


def BlackSmith(charlie_earth,b_shop_vendor):
    action('Enter('+charlie_earth.name+',Blacksmith.Door)')
    Create_item('Sword','Sword','Blacksmith.Table')
    action('WalkTo('+charlie_earth.name+',Sword)')
    action('Take('+charlie_earth.name+',Sword)')
    action('WalkTo('+charlie_earth.name+', '+b_shop_vendor.name+')')
    action('Face('+b_shop_vendor.name+','+charlie_earth.name+')')
    action('SetNarration('+charlie_earth.name+': Hi! can I get this sword please)')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')
    action('SetNarration('+b_shop_vendor.name+': Sure! Have a good day!)')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')
    action('Exit('+charlie_earth.name+',Blacksmith.Door')