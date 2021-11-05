from action import action
from create_char import create_char
from create_item import create_item

def dream():
    action('ShowMenu()')
    action('CreatePlace(Cottage, Cottage)')
    action('CreatePlace(Ruins,Ruins')

    create_char('Charlie','D','Merchant','Cottage.Bed','Spiky')
    
    action('Sleep(Charlie,Cottage.Bed)')

    create_char('Charlie1','D','King','Ruins.Exit','Spiky')

    create_item('Sword','Sword','Charlie1')
    action('Draw(Charlie1,Sword)')

    create_char('Sol1','D','HeavyArmour','Ruins.DirtPile')

    create_item('Sword1','Sword','Sol1')
    action('Draw(Sol1,Sword1)')

    create_char('Sol2','D','HeavyArmour','Ruins.Plant')

    create_item('Sword2','Sword','Sol2')
    action('Draw(Sol2,Sword2)')

    create_char('Sol3','D','HeavyArmour','Ruins.Altar')

    create_item('Sword3','Sword','Sol3')
    action('Draw(Sol3,Sword3)')

    create_char('Sol4','D','HeavyArmour','Ruins.Throne')

    create_item('Sword4','Sword','Sol4')
    action('Draw(Sol4,Sword4)')

    action('Wait(1)')
    action('HideMenu()')

    action('SetCameraFocus(Charlie1)')
    action('SetCameraMode(Track)')
    action('SetCameraMode(Follow)')
    action('Wait(2)')

    action('WalkTo(Charlie1, Sol1)')
    action('PlaySound(Draw)','False')
    action('Attack(Charlie1,Sol1)')
    action('Die(Sol1)')

    action('WalkTo(Charlie1,Sol2)')
    action('PlaySound(Draw)','False')
    action('Attack(Charlie1,Sol2)')
    action('Die(Sol2)')

    action('WalkTo(Charlie1,Sol3)')
    action('PlaySound(Draw)','False')
    action('Attack(Charlie1,Sol3)')
    action('Die(Sol3)')

    action('WalkTo(Charlie1,Sol4)')
    action('PlaySound(Draw)','False')
    action('Attack(Charlie1,Sol4)')
    action('PlaySound(Draw)','False')
    action('Attack(Sol4,Charlie1)')
    action('PlaySound(Draw)','Flase')
    action('Attack(Charlie1,Sol4)')
    action('Die(Sol4)')

    action('WalkTo(Charlie1,Ruins.Chest)')
    action('PutDown(Charlie1,Sword)')
    action('OpenFurniture(Charlie1,Ruins.Chest)')
    action('CreateEffect(Ruins.Chest,Explosion)')


def scene1():
    action('SetCameraFocus(Charlie)')
    action('Wait(1)')
    action('SetNarration(Charlie: Oh boy!.. That was a dream!.)')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')
    action('Sit(Charlie,Cottage.Bed)')
    action('SetNarration(Charlie: A boring day starts again)')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')
