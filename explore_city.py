from action import action
from call_for_help import call_for_help
from engage_fight import engage_fight
from visit_fruitshop import visit_Fruitshop

def explore_city(charlie_earth,bandit1,bandit2,bandit3):
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.Horse)')
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.WestEnd)')
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.Fountain)')
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.EastEnd)')
    action('Attack('+bandit1.name+','+charlie_earth.name+',False)')
    action('Attack('+bandit2.name+','+charlie_earth.name+',False)')
    action('MoveAway('+charlie_earth.name+')')

    action('EnableIcon(call_for_help,kneel,Charlie,"Call for help")')
    action('EnableIcon(engage_fight,fist,Charlie,"Engage fight")')
    action('EnableInput()')
    choice4(charlie_earth)
    action('DisableInput()')

def choice4(charlie_earth):
    while True:
        received=input()
        if received=='input call_for_help Charlie':
           return call_for_help(charlie_earth)
        elif received=='input engage_fight Charlie':
           return engage_fight(charlie_earth)
