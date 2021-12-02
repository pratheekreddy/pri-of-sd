from action import action

def Message(message):
    action('SetNarration('+message+')')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')