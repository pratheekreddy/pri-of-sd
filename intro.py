from action import action
from attack import attack

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
    #action('SetCameraMode(Follow)')
    action('Wait(2)')
    #player choise
    war_with_sol(charlie_dream,soldier1,soldier2,soldier3,soldier4)
    #function for sleeping gass
    # sleeping_gas(soldier1,soldier2,soldier3,soldier4)
    # function for escape
    action('WalkTo('+charlie_dream.name+',Ruins.Chest)')
    action('PutDown('+charlie_dream.name+',Sword_charlie)')
    action('OpenFurniture('+charlie_dream.name+',Ruins.Chest)')
    action('CreateEffect(Ruins.Chest,Explosion)')

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