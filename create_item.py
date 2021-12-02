# need to pass argument- item_name, item-type, position 
# to create a item and palce that item in particular position



from action import action
class Create_item:
    def __init__(self,item_name,item,position):
        self.name=item_name
        self.item=item
        action('CreateItem('+item_name+','+item+')')
        action('SetPosition('+item_name+','+position+')')