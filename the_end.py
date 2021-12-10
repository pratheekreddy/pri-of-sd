from action import action
from attack import attack
from message import Message
from start import witch

def the_end(charlie_earth):
    action('SetPosition('+charlie_earth.name+',Courtyard.Gate)')
    action('CreateEffect('+charlie_earth.name+', Resurrection)')
    Message('Charlie: You are the witch that made me come here. I must kill you so that I can return to my world!')
    Message('Witch: No dont. I did this because I love you!' )
    Message('Charlie: What you did is not love. You endagered my life and now Im gonna kill you!!')
    attack(charlie_earth.name,witch.name)
    action('Die('+witch.name+')')
    