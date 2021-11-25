# need to pass argument- name, body-type, clothing, 
# position and hairstyle in an order to create a character 

from action import action
from create_item import create_item

class Create_char:

    def __init__(self,name , body_type , clothing ,position, hair="Spiky"):
        self.name = name
        action('CreateCharacter('+name+','+body_type+')')
        action('SetClothing('+name+', '+clothing+')')
        action('SetExpression('+name+',Happy)')
        action('SetHairStyle('+name+','+hair+')')
        action('SetPosition('+name+','+position+')')
    
    def give_item(self,i_name,i_type):
        create_item(i_name,i_type,self.name)
        action('Draw('+self.name+','+i_name+')')

    def camera(self):
        action('SetCameraFocus('+self.name+')')
