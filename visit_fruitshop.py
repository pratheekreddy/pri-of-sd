from action import action
from create_item import create_item
from message import Message

def visit_Fruitshop(charlie_earth,f_shop_vendor):
    action('WalkTo('+charlie_earth+',MysteryWorld.RedHouseDoor)',False)
    create_item('Sword_t','Sword',f_shop_vendor,False)
    create_item('Apple1','Apple','FruitShop.Table',False)
    create_item('Apple2','Apple','FruitShop.Table',False)
    create_item('Apple3','Apple','FruitShop.Table',False)
    create_item('Apple4','Apple','FruitShop.Table')
    action('Enter('+charlie_earth.name+',FruitShop.Door)')
    action('Take('+charlie_earth.name+',Apple1')
    action('WalkTo('+charlie_earth.name+','+f_shop_vendor.name+')')
    Message(charlie_earth,'Hi! can I get this apple please)')
    Message(f_shop_vendor,'Nahi!')
    Message(charlie_earth,'Pardon me! I did not understand.')
    Message(f_shop_vendor,'Yaha se baahar jaao, kon aadmi ho tum')
    Message('Things get esculated and the vendor gets angry!')
    action('Draw('+f_shop_vendor.name+',Sword_t')
    action('Attack('+f_shop_vendor.name+','+charlie_earth.name+',False)')
    action('Die('+charlie_earth.name+')')
    action('Enter('+charlie_earth.name+',Mysteryworld.NorthEnd)',False)
    action('CreateEffect('+charlie_earth+',Resurrection)')
