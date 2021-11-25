#This is the Starting point of the story. 
# Configure this file in your startExperienceManager file
# Try not to logic in this file except importing files.(should follow modularized coding practice)

from intro import dream,scene1
from action import action
from create_char import Create_char
# CREATE Charactors 
action('ShowMenu()')
charlie_earth=Create_char('Charlie','D','Merchant','Cottage.Bed','Spiky')
charlie_dream=Create_char('Charlie1','D','King','Ruins.Exit','Spiky')
soldier1=Create_char('Soldier1','D','HeavyArmour','Ruins.DirtPile')
soldier2=Create_char('Soldier2','D','HeavyArmour','Ruins.Plant')
soldier3=Create_char('Soldier3','D','HeavyArmour','Ruins.Altar')
soldier4=Create_char('Soldier4','D','HeavyArmour','Ruins.Throne')
#-----------
#CREATE LOCATIONS
action('CreatePlace(Cottage, Cottage)')
action('CreatePlace(Ruins,Ruins')
#-----------

# CREATE OBJECTS OR GLOBAL VARIABLES

#------------
dream(charlie_earth,charlie_dream,soldier1,soldier2,soldier3,soldier4)
scene1(charlie_earth)

while(True):
    input(charlie_earth)