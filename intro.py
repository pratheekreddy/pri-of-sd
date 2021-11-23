from action import action
from create_char import Create_char
from create_item import create_item

def dream():
    action('ShowMenu()')
    action('CreatePlace(Cottage, Cottage)')
    action('CreatePlace(Ruins,Ruins')

    global charlie_earth
    charlie_earth=Create_char('Charlie','D','Merchant','Cottage.Bed','Spiky')
    
    action('Sleep(Charlie,Cottage.Bed)')

    global charlie_dream
    charlie_dream=Create_char('Charlie1','D','King','Ruins.Exit','Spiky')
    charlie_dream.give_item('Sword_charlie','Sword')

    soldier1=Create_char('Soldier1','D','HeavyArmour','Ruins.DirtPile')
    soldier1.give_item('Sword_sol1','Sword')

    soldier2=Create_char('Soldier2','D','HeavyArmour','Ruins.Plant')

    soldier2.give_item('Sword_sol3','Sword','Sol2')

    soldier3=Create_char('Soldier3','D','HeavyArmour','Ruins.Altar')

    soldier3.give_item('Sword3','Sword','Sol3')

    soldier4=Create_char('Soldier4','D','HeavyArmour','Ruins.Throne')

    soldier4.give_item('Sword4','Sword','Sol4')

    action('Wait(1)')
    action('HideMenu()')

    charlie_dream.camera()
    action('SetCameraMode(Track)')
    action('SetCameraMode(Follow)')
    action('Wait(2)')

    attack(charlie_dream.name,soldier1.name)

    attack(charlie_dream.name,soldier2.name)

    attack(charlie_dream.name,soldier3.name)

    attack(charlie_dream.name,soldier4.name)

    action('WalkTo('+charlie_dream.name+',Ruins.Chest)')
    action('PutDown('+charlie_dream.name+',Sword)')
    action('OpenFurniture('+charlie_dream.name+',Ruins.Chest)')
    action('CreateEffect(Ruins.Chest,Explosion)')

def attack(x,y):
    action('WalkTo('+x+','+y+')')
    action('PlaySound(Draw)','False')
    action('Attack('+x+','+y+')')
    action('Die('+y+')')

def scene1():
    action('SetCameraFocus('+charlie_earth.name+')')
    action('Wait(1)')
    action('SetNarration(Charlie: Oh boy!.. That was a dream!.)')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')
    action('Sit('+charlie_earth.name+',Cottage.Bed)')
    action('SetNarration('+charlie_earth.name+': A boring day starts again)')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')
