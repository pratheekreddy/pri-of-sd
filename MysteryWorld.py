from action import action
from explore_city import explore_city
from visit_fruitshop import visit_Fruitshop


def MysteryWorld(charlie_earth):
    action('SetPosition('+charlie_earth.name+',P_MysteryWorld.NorthEnd)')
    action('CreateEffect('+charlie_earth.name+',Resurrection)')

    action('EnableIcon(Explore_city,city,Charlie,"Explore city")')
    action('EnableIcon(Fruit_shop,apple,Charlie,"Go to fruit shop")')
    action('EnableInput()')
    choice4(charlie_earth)
    action('DisableInput()')

def choice4(charlie_earth):
    while True:
        received=input()
        if received=='input Explore_city Charlie':
           return explore_city(charlie_earth)
        elif received=='input Fruit_shop Charlie':
           return visit_Fruitshop(charlie_earth)