from MysteryWorld import MysteryWorld
from action import action
from create_item import Create_item
from message import Message
from start import f_shop_vendor

def visit_Fruitshop(charlie_earth):
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.RedHouseDoor)')
    action('Enter('+charlie_earth.name+',FruitShop.Door)')
    f_shop_vendor.give_item('Sword_t','Sword')
    action('Take('+charlie_earth.name+',Apple1_fruit)')
    action('WalkTo('+charlie_earth.name+','+f_shop_vendor.name+')')
    Message('Charlie: Hi! can I get this apple please)')
    Message('Vendor: Nahi!')
    Message('Charlie: Pardon me! I did not understand.')
    Message('Vendor: Yaha se baahar jaao, kon aadmi ho tum')
    Message('Things get esculated and the vendor gets angry!')
    f_shop_vendor.expression('angry')
    action('Draw('+f_shop_vendor.name+',Sword_t')
    action('Attack('+f_shop_vendor.name+','+charlie_earth.name+')')
    action('Die('+charlie_earth.name+')')
    MysteryWorld(charlie_earth)
