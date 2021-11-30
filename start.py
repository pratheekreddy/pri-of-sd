#This is the Starting point of the story. 
# Configure this file in your startExperienceManager file
# Try not to logic in this file except importing files.(should follow modularized coding practice)

from action import action
from Class.create_char import Create_char
from intro import dream
from begining import scene1
from alchemy_store import AlchemyStore
from blacksmith import BlackSmith
from MysteryWorld import MysteryWorld
from visit_fruitshop import visit_Fruitshop
from explore_city import explore_city
from Class.Places import Place


#CREATE LOCATIONS
Cottage=Place('Cottage', 'Cottage')
Ruins=Place('Ruins','Ruins')
Bridge=Place('Bridge','Bridge')
AlchemyShop=Place('AlchemyShop','AlchemyShop')
Blacksmith=Place('Blacksmith','Blacksmith')
FruitShop=Place('FruitShop','AlchemyShop')
P_MysteryWorld=Place('MysteryWorld','City')
#-----------

action('ShowMenu()')

# CREATE Charactors 
charlie_earth=Create_char('Charlie','D','Merchant','Cottage.Bed','Spiky')
charlie_dream=Create_char('Charlie1','D','King','Ruins.Exit','Spiky')
soldier1=Create_char('Soldier1','D','HeavyArmour','Ruins.DirtPile')
soldier2=Create_char('Soldier2','D','HeavyArmour','Ruins.Plant')
soldier3=Create_char('Soldier3','D','HeavyArmour','Ruins.Altar')
soldier4=Create_char('Soldier4','D','HeavyArmour','Ruins.Throne')
a_shop_vendor=Create_char('a_shop_vendor','A','Merchant','AlchemyShop.Bar')
b_shop_vendor=Create_char('b_shop_vendor','F','Merchant','Blacksmith.Anvil')
bandit1=Create_char('bandit1','B','Bandit','MysteryWorld.EastEnd')
bandit2=Create_char('bandit2','B','Bandit','MysteryWorld.EastEnd')
bandit3=Create_char('bandit3','B','Bandit','MysteryWorld.EastEnd')
#-----------

# CREATE OBJECTS OR GLOBAL VARIABLES

#------------
dream(charlie_earth,charlie_dream,soldier1,soldier2,soldier3,soldier4)
scene1(charlie_earth)
AlchemyStore(charlie_earth,a_shop_vendor)
BlackSmith(charlie_earth,b_shop_vendor)



while(True):
    input(charlie_earth)