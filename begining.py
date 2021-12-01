
from action import action
from message import Message

def scene1(charlie_earth):
    action('SetCameraFocus('+charlie_earth.name+')')
    Message('Charlie: Oh boy!.. That was a dream!.')
    action('Sit('+charlie_earth.name+',Cottage.Bed)')
    Message('Charlie: : A boring day starts again')
    action('Exit('+charlie_earth.name+',Cottage.Door)')
    action('Enter('+charlie_earth.name+',Bridge.NorthEnd)')