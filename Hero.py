from action import action
from create_char import Create_char
class Hero(Create_char):
    _shared = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def getinstance(cls,name, body_type , clothing ,position,items, hair="Spiky"):
        if cls._shared is None:
            cls._shared=cls.__new__(cls)
            # cls._shared.name=name
            Create_char.__init__(cls,name,body_type,clothing,position)
            cls._shared.items=items
            # action('CreateCharacter('+name+','+body_type+')')
            # action('SetClothing('+name+', '+clothing+')')
            # action('SetExpression('+name+',Happy)')
            # action('SetHairStyle('+name+','+hair+')')
            # action('SetPosition('+name+','+position+')')
        return cls._shared

hero=Hero.getinstance('Charlie','D','Merchant','Cottage.Bed','book')
print(hero.items)
print(hero.name)