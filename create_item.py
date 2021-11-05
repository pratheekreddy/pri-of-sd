# need to pass argument- item_name, item-type, position 
# to create a item and palce that item in particular position



from action import action

def create_item(item_name,item,position):
    action('CreateItem('+item_name+','+item+')')
    action('SetPosition('+item_name+','+position+')')