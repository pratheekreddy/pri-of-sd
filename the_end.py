from action import action
from attack import attack
from message import Message

def the_end(charlie_earth,witch):
    action('SetPosition('+charlie_earth.name+',Courtyard.Gate)')
    action('CreateEffect('+charlie_earth.name+', Resurrection)')
    Message('Charlie: You are the witch that made me come here. I must kill you so that I can return to my world!')
    Message('Witch: No dont. I did this because I love you!' )
    Message('Charlie: What you did is not love. You endagered my life and now Im gonna kill you!!')
    action('Draw('+charlie_earth.name+',Sword_b)')
    attack(charlie_earth.name,witch.name)
    action('Die('+witch.name+')')
    Message('Charlie: Now that I killed the witch with the spelled dagger I can return to my world.')
    Message('The END')