from action import action
from create_item import Create_item
from message import Message
from the_end import the_end


def find_book(charlie_earth,witch):
    Message('Since you have a daggger find the book and use the spell to activate sword power')
    action('Enter('+charlie_earth.name+',AlchemyShop.Door)')
    EvilBook2=Create_item('EvilBook2','EvilBook','AlchemyShop.Bookshelf')
    action('WalkTo('+charlie_earth.name+',EvilBook2)')
    action('Take('+charlie_earth.name+',EvilBook2)')
    Message('Charlie reads the spell: Abrakha Dhabra Boom.')
    action('SetPosition(Sword_b,'+charlie_earth.name+')',False)
    action('EnableEffect(Spiralflame,Sword_b)')
    action('Exit('+charlie_earth.name+',AlchemyShop.Door')
    the_end(charlie_earth,witch)