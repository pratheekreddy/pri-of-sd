from action import action

def Message(Name,message):
    action('SetNarration('+Name+': '+message+')')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')
def Message(message):
    action('SetNarration('+message+')')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')