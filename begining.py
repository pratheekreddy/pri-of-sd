from action import action
from alchemy_store import AlchemyStore
from message import Message
from blacksmith import BlackSmith



def scene1(charlie_earth):
    action('SetCameraFocus('+charlie_earth.name+')')
    Message('Charlie: Oh boy!.. That was a dream!.')
    action('Sit('+charlie_earth.name+',Cottage.Bed)')
    home(charlie_earth)

def home(charlie_earth):
    Message('Charlie: : A boring day starts again')
    action('Exit('+charlie_earth.name+',Cottage.Door)')
    action('Enter('+charlie_earth.name+',Bridge.NorthEnd)')
    
    action('EnableIcon(alchemystore,cottage,Charlie,"Go to Alchemy store")')
    action('EnableIcon(blacksmith,anvil,Charlie,"Go to Blacksmith store")')
    action('Right click on Charlie to get choice bar')
    action('EnableInput()')
    choice2(charlie_earth)
    action('DisableInput()')

def choice2(charlie_earth):
    while True:
        received=input()
        if received=='input alchemystore Charlie':
           return AlchemyStore(charlie_earth)
        elif received=='input blacksmith Charlie':
           return BlackSmith(charlie_earth)