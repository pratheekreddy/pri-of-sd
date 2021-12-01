#This is the Starting point of the story. 
# Configure this file in your startExperienceManager file
# Try not to logic in this file except importing files.(should follow modularized coding practice)

from MysteryWorld import MysteryWorld
from action import action
from create_char import Create_char
from explore_city import explore_city
from intro import dream
from begining import scene1
from alchemy_store import AlchemyStore
from blacksmith import BlackSmith
from Places import Place
from visit_fruitshop import visit_Fruitshop


#CREATE LOCATIONS
Cottage=Place('Cottage', 'Cottage')
Ruins=Place('Ruins','Ruins')
Bridge=Place('Bridge','Bridge')
AlchemyShop=Place('AlchemyShop','AlchemyShop')
Blacksmith=Place('Blacksmith','Blacksmith')
FruitShop=Place('FruitShop','AlchemyShop')
P_MysteryWorld=Place('P_MysteryWorld','City')
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
f_shop_vendor=Create_char('f_shop_vendor','A','Peasant','FruitShop.Bar')
bandit1=Create_char('bandit1','B','LightArmour','P_MysteryWorld.EastEnd')
bandit2=Create_char('bandit2','B','LightArmour','P_MysteryWorld.EastEnd')
bandit3=Create_char('bandit3','B','LightArmour','P_MysteryWorld.EastEnd')
emily=Create_char('Emily','c','Bandit','P_MysteryWorld.Horse')
#-----------

# CREATE OBJECTS OR GLOBAL VARIABLES

#------------
dream(charlie_earth,charlie_dream,soldier1,soldier2,soldier3,soldier4)
scene1(charlie_earth)
AlchemyStore(charlie_earth,a_shop_vendor)
#BlackSmith(charlie_earth,b_shop_vendor)
MysteryWorld(charlie_earth)
visit_Fruitshop(charlie_earth,f_shop_vendor)
explore_city(charlie_earth,bandit1,bandit2,bandit3)


while(True):
    input(charlie_earth)