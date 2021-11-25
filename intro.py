from action import action
from create_item import create_item

def dream(charlie_earth,charlie_dream,soldier1,soldier2,soldier3,soldier4):
    
    action('Sleep('+charlie_earth.name+',Cottage.Bed)')
    charlie_dream.give_item('Sword_charlie','Sword')

    soldier1.give_item('Sword_sol1','Sword')

    soldier2.give_item('Sword_sol3','Sword')


    soldier3.give_item('Sword3','Sword')

    soldier4.give_item('Sword4','Sword')

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

def scene1(charlie_earth):
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
    action('Exit('+charlie_earth.name+',Cottage.Door)')
    action('Enter('+charlie_earth.name+',Bridge.NorthEnd)')
