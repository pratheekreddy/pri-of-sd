from action import action
from call_for_help import call_for_help
from engage_fight import engage_fight
from start import bandit1,bandit2,bandit3
from message import Message

def explore_city(charlie_earth):
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.WestEnd)')
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.Fountain)')
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.EastEnd)')
    action('Attack('+bandit1.name+','+charlie_earth.name+',False)')
    action('Attack('+bandit2.name+','+charlie_earth.name+',False)')

    action('EnableIcon(call_for_help,kneel,Charlie,"Call for help")')
    action('EnableIcon(engage_fight,fist,Charlie,"Engage fight")')
    action('EnableInput()')
    Message('Right click on charlie for choice  bar.')
    choice5(charlie_earth)
    action('DisableInput()')

def choice5(charlie_earth):
    while True:
        received=input()
        if received=='input call_for_help Charlie':
           return call_for_help(charlie_earth)
        elif received=='input engage_fight Charlie':
           return engage_fight(charlie_earth)