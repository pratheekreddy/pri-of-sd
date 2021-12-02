from action import action

class Place:
    def __init__(self,name,type):
        self.name=name
        self.type=type
        action('CreatePlace('+name+', '+type+')')