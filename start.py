#This is the Starting point of the story. 
# Configure this file in your startExperienceManager file
# Try not to logic in this file except importing files.(should follow modularized coding practice)

from blacksmith import BlackSmith
from intro import dream,scene1
from alchemy_store import AlchemyStore
from action import action
from create_char import Create_char

#CREATE LOCATIONS
action('CreatePlace(Cottage, Cottage)')
action('CreatePlace(Ruins,Ruins')
action('CreatePlace(Bridge,Bridge')
action('CreatePlace(AlchemyShop,AlchemyShop)')
action('CreatePlace(Blacksmith,Blacksmith)')
action('CreatePlace(Mysteryworld,City)')
action('CreatePlace(FruitShop,AlchemyShop')
#-----------

# CREATE Charactors 
action('ShowMenu()')
charlie_earth=Create_char('Charlie','D','Merchant','Cottage.Bed','Spiky')
charlie_dream=Create_char('Charlie1','D','King','Ruins.Exit','Spiky')
soldier1=Create_char('Soldier1','D','HeavyArmour','Ruins.DirtPile')
soldier2=Create_char('Soldier2','D','HeavyArmour','Ruins.Plant')
soldier3=Create_char('Soldier3','D','HeavyArmour','Ruins.Altar')
soldier4=Create_char('Soldier4','D','HeavyArmour','Ruins.Throne')

a_shop_vendor=Create_char('a_shop_vendor','A','Merchant','AlchemyShop.Bar')
b_shop_vendor=Create_char('b_shop_vendor','F','Merchant','Blacksmith.Anvil')

f_shop_vendor=Create_char('f_shop_vendor','F','Peasant','FruitShop.Bar')
#-----------

# CREATE OBJECTS OR GLOBAL VARIABLES

#------------
dream(charlie_earth,charlie_dream,soldier1,soldier2,soldier3,soldier4)
scene1(charlie_earth)
BlackSmith(charlie_earth,b_shop_vendor)
AlchemyStore(charlie_earth,a_shop_vendor)


while(True):
    input(charlie_earth)