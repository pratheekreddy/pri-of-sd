from action import action
from attack import attack
from message import Message

def the_end(charlie_earth,witch):
    action('SetPosition('+charlie_earth.name+',Courtyard.Gate)')
    action('CreateEffect('+charlie_earth.name+', Resurrection)')
    Message('Charlie: You are the witch that made me come here. I must kill you so that I can return to my world!')
    charlie_earth.camera()
    Message('Witch: No dont. I did this because I love you!' )
    Message('Charlie: What you did is not love. You endagered my life and now Im gonna kill you!!')
    action('Draw('+charlie_earth.name+',Sword_b)')
    action('SetCameraMode(Track)')
    action('Face(witch,Charlie')
    attack(charlie_earth.name,witch.name)
    action('Die('+witch.name+')')
    action('PutDown('+charlie_earth.name+',Sword_b)')
    Message('Charlie: Now that I killed the witch with the spelled dagger I can return to my world.')
    Message('The END')

    action('CreateEffect(Death,'+charlie_earth.name+')')
    charlie_earth.set_position('end.Bed')
    charlie_earth.set_clothes('Peasant')
    action('SetNarration(Oh boy! That was a dream.)')
    action('ShowNarration()')
