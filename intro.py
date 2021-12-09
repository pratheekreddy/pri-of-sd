from action import action
from attack import attack
from begining import scene1

def dream(charlie_earth,charlie_dream,soldier1,soldier2,soldier3,soldier4):
    action('Sleep('+charlie_earth.name+',Cottage.Bed)')
    charlie_dream.give_item('Sword_charlie','Sword')
    soldier1.give_item('Sword_sol1','Sword')
    soldier2.give_item('Sword_sol3','Sword')
    soldier3.give_item('Sword3','Sword')
    soldier4.give_item('Sword4','Sword')
    action('HideMenu()')

    charlie_dream.camera()
    action('SetCameraMode(Follow)')
    
    action('EnableIcon(war_with_sol,sword,Charlie1,"Kill with Sword")')
    action('EnableIcon(sleeping_gas,potion,Charlie1,"Sleeping Gas ")')
    action('EnableIcon(sneak,helm,Charlie1,"Sneak to the chest")')
    action('EnableInput()')
    choice1(charlie_earth,charlie_dream,soldier1,soldier2,soldier3,soldier4)
    action('DisableInput()')

    action('SetCameraMode(Track)')
    action('WalkTo('+charlie_dream.name+',Ruins.Chest)')
    action('PutDown('+charlie_dream.name+',Sword_charlie)')
    action('OpenFurniture('+charlie_dream.name+',Ruins.Chest)')
    action('CreateEffect(Ruins.Chest,Explosion)')
    scene1(charlie_earth)


def war_with_sol(charlie_dream,soldier1,soldier2,soldier3,soldier4):
    attack(charlie_dream.name,soldier1.name)
    attack(charlie_dream.name,soldier2.name)

    attack(charlie_dream.name,soldier3.name)

    attack(charlie_dream.name,soldier4.name)

def sleeping_gas(soldier1,soldier2,soldier3,soldier4):
    action('CreateEffect('+soldier1.name+',Brew)',False)
    action('Die('+soldier1.name+')',False)
    action('CreateEffect('+soldier2.name+',Brew)',False)
    action('Die('+soldier2.name+')',False)
    action('CreateEffect('+soldier3.name+',Brew)',False)
    action('Die('+soldier3.name+')',False)
    action('CreateEffect('+soldier4.name+',Brew)',False)
    action('Die('+soldier4.name+')',False)

def Sneak(charlie_dream):
    action('CreateEffect('+charlie_dream.name+', Aura)')
    action('SetPosition('+charlie_dream.name+',Ruins.Chest')

def choice1(charlie_earth,charlie_dream,soldier1,soldier2,soldier3,soldier4):
    while True:
        received=input()
        if received=='input war_with_sol Charlie1':
           return war_with_sol(charlie_earth,charlie_dream,soldier1,soldier2,soldier3,soldier4)
        elif received=='input sleeping_gas Charlie1':
           return sleeping_gas(soldier1,soldier2,soldier3,soldier4)
        elif received=='input sneak Charlie1':
            return Sneak(charlie_dream)