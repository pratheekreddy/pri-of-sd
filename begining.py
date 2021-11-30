
from action import action
from message import Message

def scene1(charlie_earth):
    action('SetCameraFocus('+charlie_earth.name+')')
    Message(charlie_earth.name+': Oh boy!.. That was a dream!.')
    action('Sit('+charlie_earth.name+',Cottage.Bed)')
    action('SetNarration('+charlie_earth.name+': A boring day starts again)')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')
    action('Exit('+charlie_earth.name+',Cottage.Door)')
    action('Enter('+charlie_earth.name+',Bridge.NorthEnd)')
