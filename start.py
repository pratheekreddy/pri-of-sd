#This is the Starting point of the story. 
# Configure this file in your startExperienceManager file
# Try not to logic in this file except importing files.(should follow modularized coding practice)

# from MysteryWorld import MysteryWorld
from action import action
from attack import attack
from message import Message, Message1, d_box
from create_char import Create_char
from create_item import Create_item
from Places import Place
from attack import attack
from find_dager import find_dager
from find_book import find_book
#CREATE LOCATIONS
Cottage=Place('Cottage', 'Cottage')
Ruins=Place('Ruins','Ruins')
Bridge=Place('Bridge','Bridge')
AlchemyShop=Place('AlchemyShop','AlchemyShop')
Blacksmith=Place('Blacksmith','Blacksmith')
FruitShop=Place('FruitShop','AlchemyShop')
P_MysteryWorld=Place('P_MysteryWorld','City')
Courtyard=Place('Courtyard','Courtyard')
end = Place('end','Cottage')
#-----------
action('SetTitle(\"Witch''s Gambit\")')
action('ShowMenu()')
action('SetNarration(Loading resources...)')
action('ShowNarration()')

# CREATE Charactors 
charlie_earth=Create_char('Charlie','D','Peasant','Cottage.Bed','Spiky')
charlie_dream=Create_char('Charlie1','D','King','Ruins.Exit','Spiky')
soldier1=Create_char('Soldier1','D','HeavyArmour','Ruins.DirtPile')
soldier2=Create_char('Soldier2','D','HeavyArmour','Ruins.Plant')
soldier3=Create_char('Soldier3','D','HeavyArmour','Ruins.Altar')
soldier4=Create_char('Soldier4','D','HeavyArmour','Ruins.Throne')
a_shop_vendor=Create_char('a_shop_vendor','A','Beggar','AlchemyShop.Bar')
b_shop_vendor=Create_char('b_shop_vendor','F','Beggar','Blacksmith.Anvil')
f_shop_vendor=Create_char('f_shop_vendor','A','Merchant','FruitShop.Bar')
bandit1=Create_char('bandit1','B','LightArmour','P_MysteryWorld.EastEnd')
bandit2=Create_char('bandit2','B','LightArmour','P_MysteryWorld.EastEnd')
bandit3=Create_char('bandit3','B','LightArmour','P_MysteryWorld.EastEnd')
emily=Create_char('Emily','c','Bandit','P_MysteryWorld.Horse')
witch=Create_char('witch','E','Witch','Courtyard.Fountain','Pony')
#-----------

# CREATE OBJECTS OR GLOBAL VARIABLES

#------------
# dream(charlie_earth,charlie_dream,soldier1,soldier2,soldier3,soldier4)

def dream(charlie_earth,charlie_dream,soldier1,soldier2,soldier3,soldier4):
    action('Sleep('+charlie_earth.name+',Cottage.Bed)')
    charlie_dream.give_item('Sword_charlie','Sword')
    soldier1.give_item('Sword_sol1','Sword')
    soldier2.give_item('Sword_sol3','Sword')
    soldier3.give_item('Sword3','Sword')
    soldier4.give_item('Sword4','Sword')
    action('HideNarration()')
    if(input()=='input Selected Start'):
        action('HideMenu()')
    Message('Player controls: Right click on a highlighted item or character to see the choice bar and click on a choice')

    charlie_dream.camera()
    action('SetCameraMode(Track)')
    Message('Right click on character Charlie to get the choice bar.')
    action('EnableIcon(war_with_sol,sword,Charlie1,"Kill with Sword")')
    action('EnableIcon(sleeping_gas,potion,Charlie1,"Sleeping Gas")')
    action('EnableIcon(sneak,helm,Charlie1,"Sneak to the chest")')
    
    action('EnableInput()')
    choice1(charlie_earth,charlie_dream,soldier1,soldier2,soldier3,soldier4)
    action('DisableInput()')

    action('SetCameraMode(Track)')
    action('WalkTo('+charlie_dream.name+',Ruins.Chest)')
    action('PutDown('+charlie_dream.name+',Sword_charlie)')
    action('OpenFurniture('+charlie_dream.name+',Ruins.Chest)')
    action('CreateEffect(Ruins.Chest,Explosion)')
    action('CreateEffect(Ruins.Chest,Explosion)')
    action('Wait(1)')
    # from begining import scene1
    scene1(charlie_earth)


def war_with_sol(charlie_dream,soldier1,soldier2,soldier3,soldier4):
    action('SetCameraMode(Follow)')
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
    Message('Charlie: Kaboom!! take me to the chest')
    action('CreateEffect('+charlie_dream.name+', Aura)')
    action('SetPosition('+charlie_dream.name+',Ruins.Chest')
    action('CreateEffect('+charlie_dream.name+', Aura)')


def choice1(charlie_earth,charlie_dream,soldier1,soldier2,soldier3,soldier4):
    while True:
        received=input()
        if received=='input war_with_sol Charlie1':
           return war_with_sol( charlie_dream,soldier1,soldier2,soldier3,soldier4)
        elif received=='input sleeping_gas Charlie1':
           return sleeping_gas(soldier1,soldier2,soldier3,soldier4)
        elif received=='input sneak Charlie1':
            return Sneak(charlie_dream)

def scene1(charlie_earth):
    action('SetCameraFocus('+charlie_earth.name+')')
    Message('Charlie: Oh boy!.. That was a dream!.')
    action('Sit('+charlie_earth.name+',Cottage.Bed)')
    home(charlie_earth)

def home(charlie_earth):
    Message('Charlie: A boring day starts again')
    action('Exit('+charlie_earth.name+',Cottage.Door)')
    action('Enter('+charlie_earth.name+',Bridge.NorthEnd)')
    
    action('EnableIcon("alchemystore",cottage,Charlie,"Go to Alchemy store")')
    action('EnableIcon("blacksmith",anvil,Charlie,"Go to Blacksmith store")')
    Message('Right click on Charlie to get choice bar')
    action('EnableInput()')
    choice2(charlie_earth)
    action('DisableIcon("alchemystore",Charlie)')
    action('DisableIcon("blacksmith",Charlie)')
    action('DisableInput()')

def choice2(charlie_earth):
    while True:
        received=input()
        if received=='input alchemystore Charlie':
           return AlchemyStore(charlie_earth)
        elif received=='input blacksmith Charlie':
           return BlackSmith(charlie_earth)

def BlackSmith(charlie_earth):
    action('Enter('+charlie_earth.name+',Blacksmith.Door)')
    Sword_b=Create_item('Sword_b','Sword','Blacksmith.Table')
    action('WalkTo('+charlie_earth.name+',Sword_b)')
    action('Take('+charlie_earth.name+',Sword_b)')
    charlie_earth.item='dagger'
    action('WalkTo('+charlie_earth.name+', '+b_shop_vendor.name+')')
    action('Face('+b_shop_vendor.name+','+charlie_earth.name+')')
    d_box(charlie_earth.name,b_shop_vendor.name)
    Message1('Charlie: Hi! can I get this sword please')
    Message1('Vendor: Sure! Have a good day!')
    action('HideDialog()')
    action('Exit('+charlie_earth.name+',Blacksmith.Door')
    MysteryWorld(charlie_earth)

def AlchemyStore(charlie_earth):
    action('Enter('+charlie_earth.name+',AlchemyShop.Door)')
    Apple=Create_item('Apple','Apple','AlchemyShop.Table')
    EvilBook=Create_item('EvilBook','EvilBook','AlchemyShop.Bookshelf')
    Bag=Create_item('Bag','Bag','AlchemyShop.Bar')
    action('EnableIcon("buy_apple",apple,Charlie,"Buy apple")')
    action('EnableIcon("buy_bag",lockedchest,Charlie,"Buy Bag")')
    action('EnableIcon("buy_book",evilbook,Charlie,"Buy Book")')
    action('EnableInput()')
    Message('System: Right click on charlie and select an icon.')
    choice3(charlie_earth)
    action('DisableIcon("buy_bag",Charlie)')
    action('DisableIcon("buy_apple",Charlie)')
    action('DisableIcon("buy_book",Charlie)')
    action('DisableInput()')
    

def buy_apple(charlie_earth):
    action('WalkTo('+charlie_earth.name+',Apple)')
    action('Take('+charlie_earth.name+',Apple)')
    action('WalkTo('+charlie_earth.name+', '+a_shop_vendor.name+')')
    action('Face('+a_shop_vendor.name+','+charlie_earth.name+')')
    d_box(charlie_earth.name,a_shop_vendor.name)
    Message1('Charlie: Hi! can I get this apple')
    Message1('Vendor: Sure! Have a good day!')
    action('HideDialog()')
    action('Exit('+charlie_earth.name+',AlchemyShop.Door)')
    Message('Charlie goes back home after buying an apple and another boring day starts again!')
    action('SetPosition('+charlie_earth.name+',Cottage.Bed)')
    home(charlie_earth)

def buy_bag(charlie_earth):
    action('WalkTo('+charlie_earth.name+',Bag)')
    action('Take('+charlie_earth.name+',Bag)')
    action('WalkTo('+charlie_earth.name+', '+a_shop_vendor.name+')')
    action('Face('+a_shop_vendor.name+','+charlie_earth.name+')')
    d_box(charlie_earth.name,a_shop_vendor.name)
    Message1('Charlie: Hi! can I get this bag')
    Message1('Vendor: Sure! Have a good day!')
    action('HideDialog()')
    action('Exit('+charlie_earth.name+',AlchemyShop.Door)')
    Message('Charlie goes back home after buying a bag and another boring day starts again!')
    action('SetPosition('+charlie_earth.name+',Cottage.Bed)')
    home(charlie_earth)

def buy_book(charlie_earth):
    action('WalkTo('+charlie_earth.name+',EvilBook)')
    action('Take('+charlie_earth.name+',EvilBook)')
    action('WalkTo('+charlie_earth.name+', '+a_shop_vendor.name+')')
    action('Face('+a_shop_vendor.name+','+charlie_earth.name+')')
    d_box(charlie_earth.name,a_shop_vendor.name)
    Message1('Charlie: Hi! can I get this book.')
    Message1('Vendor: Sure! Have a good day!')
    action('HideDialog()')
    action('Exit('+charlie_earth.name+',AlchemyShop.Door)')
    charlie_earth.item='book'
    Message('Oh boy! You picked an "Evil book" so now you will be summoned to the mystery world!')
    MysteryWorld(charlie_earth)

def choice3(charlie_earth):
    while True:
        received=input()
        if received=='input buy_apple Charlie':
           return buy_apple(charlie_earth)
        elif received=='input buy_bag Charlie':
           return buy_bag(charlie_earth)
        elif received=='input buy_book Charlie':
            return buy_book(charlie_earth)

def MysteryWorld(charlie_earth):
    charlie_earth.expression('happy')
    f_shop_vendor.expression('happy')
    action('SetPosition('+charlie_earth.name+',P_MysteryWorld.NorthEnd)')
    action('CreateEffect('+charlie_earth.name+',Resurrection)')

    action('EnableIcon("clothing1",armour,Charlie,"Wear Armour")')
    action('EnableIcon("clothing2",dress,Charlie,"Wear new clothes")')
    action('EnableInput()')
    Message('Right click on charlie for choice bar.')
    clothes(charlie_earth)
    action('DisableInput()')
    action('DisableIcon("clothing1",Charlie)')
    action('DisableIcon("clothing2",Charlie)')


    action('EnableIcon("Explore_city",city,Charlie,"Explore city")')
    action('EnableIcon("Fruit_shop",apple,Charlie,"Go to fruit shop")')
    action('EnableInput()')
    Message('Right click on charlie for choice bar.')
    choice4(charlie_earth)
    action('DisableInput()')
    action('DisableIcon("Explore_city",Charlie)')
    action('DisableIcon("Fruit_shop",Charlie)')

def choice4(charlie_earth):
    while True:
        received=input()
        if received=='input Explore_city Charlie':
           return explore_city(charlie_earth)
        elif received=='input Fruit_shop Charlie':
           return visit_Fruitshop(charlie_earth)

def clothes(charlie_earth):
    while True:
        received=input()
        if received=='input clothing1 Charlie':
           return charlie_earth.set_clothes('HeavyArmour')
        elif received=='input clothing2 Charlie':
            return charlie_earth.set_clothes('Priest')

def explore_city(charlie_earth):
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.WestEnd)')
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.Fountain)')
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.EastEnd)')
    action('Attack('+bandit1.name+','+charlie_earth.name+',False)')
    action('Face('+charlie_earth.name+','+bandit1.name+')')
    action('Attack('+bandit2.name+','+charlie_earth.name+',False)')

    action('EnableIcon("call_for_help",kneel,Charlie,"Call for help")')
    action('EnableIcon("engage_fight",fist,Charlie,"Engage fight")')
    action('EnableInput()')
    Message('Right click on charlie for choice  bar.')
    choice5(charlie_earth)
    action('DisableIcon("call_for_help",Charlie)')
    action('DisableIcon("engage_fight",Charlie)')
    action('DisableInput()')

def choice5(charlie_earth):
    while True:
        received=input()
        if received=='input call_for_help Charlie':
           return call_for_help(charlie_earth)
        elif received=='input engage_fight Charlie':
           return engage_fight(charlie_earth)

def call_for_help(charlie_earth):
    Message('Charlie: HELP!! HELP!! HELP!!')
    attack(emily.name,bandit1.name)
    attack(emily.name,bandit2.name)
    attack(emily.name,bandit3.name)
    d_box(charlie_earth.name,emily.name)
    Message1('Charlie: Thank you soo much for rescuing me!. You are my hero!')
    Message1('Emily: I am Emily!')
    Message1('Charlie: I am Charlie!')
    Message1('Emily: Are you new here?')
    Message1('Charlie: Yes I am lost. I dont know how i got here.')
    Message1('Emily: Thats weird! You are not from this world. I guess this happened to you because of the witch.')
    Message1('Charlie: OMG! What should I do now?')
    Message1('Emily: We have to find the witch and kill her with the dagger and the spell from the book activates dagger power.')
    action('HideDialog()')

    if charlie_earth.item=='book':
        Message('Since I have the Evil book I need to find the dagger.')
        find_dager(charlie_earth,witch)
    elif charlie_earth.item=='dagger':
        Message('Since I have the dagger I have to find the Evil book')
        find_book(charlie_earth,witch)



def visit_Fruitshop(charlie_earth):
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.RedHouseDoor)')
    action('Enter('+charlie_earth.name+',FruitShop.Door)')
    f_shop_vendor.give_item('Sword_t','Sword')
    action('Take('+charlie_earth.name+',Apple1_fruit)')
    action('WalkTo('+charlie_earth.name+','+f_shop_vendor.name+')')
    d_box(charlie_earth.name,f_shop_vendor.name)
    Message1('Charlie: Hi! can I get this apple please)')
    Message1('Vendor:kya!! - what!')
    f_shop_vendor.expression('angry')
    charlie_earth.expression('scared')
    Message1('Charlie: Pardon me! I did not understand.')
    Message1('Vendor: kya bath kar rahe ho??? - what are you talking???')
    Message1('Things get esculated and the vendor gets angry!')
    action('HideDialog()')
    action('Draw('+f_shop_vendor.name+',Sword_b')
    action('Attack('+f_shop_vendor.name+','+charlie_earth.name+')')
    action('Die('+charlie_earth.name+')')
    MysteryWorld(charlie_earth)


def engage_fight(charlie_earth):
    action('Attack('+charlie_earth.name+','+bandit1.name+')',False)
    action('Attack('+bandit2.name+','+charlie_earth.name+')',False)
    action('Attack('+bandit3.name+','+charlie_earth.name+')')
    action('Attack('+bandit1.name+','+charlie_earth.name+')')
    action('Die('+charlie_earth.name+')')
    MysteryWorld(charlie_earth)



dream(charlie_earth,charlie_dream,soldier1,soldier2,soldier3,soldier4)
while(True):
    input(charlie_earth)