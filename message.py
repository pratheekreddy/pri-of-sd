from action import action
from attack import attack

def Message(message):
    action('SetNarration('+message+')')
    action('ShowNarration()')
    action('Wait(3)')
    action('HideNarration()')
def d_box(a,b):
    action('ShowDialog()')
    action('SetLeft('+a+')')
    action('SetRight('+b+')')
def Message1(m):
    action('SetDialog('+m+')')
    action('Wait(5)')