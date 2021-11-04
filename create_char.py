from action import action

def create_char(name , body_type , clothing ,position, hair="Spiky"):
    action('CreateCharacter('+name+','+body_type+')')
    action('SetClothing('+name+', '+clothing+')')
    action('SetExpression('+name+',Happy)')
    action('SetHairStyle('+name+','+hair+')')
    action('SetPosition('+name+','+position+')')
