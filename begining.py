from action import action
# from alchemy_store import AlchemyStore
from message import Message
# from blacksmith import BlackSmith
from create_item import Create_item
from start import a_shop_vendor,f_shop_vendor,b_shop_vendor
from start import bandit1,bandit2,bandit3,emily
from attack import attack
from message import Message, Message1, d_box
from the_end import the_end
from find_dager import find_dager


def scene1(charlie_earth):
    action('SetCameraFocus('+charlie_earth.name+')')
    Message('Charlie: Oh boy!.. That was a dream!.')
    action('Sit('+charlie_earth.name+',Cottage.Bed)')
    home(charlie_earth)

def home(charlie_earth):
    Message('Charlie: : A boring day starts again')
    action('Exit('+charlie_earth.name+',Cottage.Door)')
    action('Enter('+charlie_earth.name+',Bridge.NorthEnd)')
    
    action('EnableIcon(alchemystore,cottage,Charlie,"Go to Alchemy store")')
    action('EnableIcon(blacksmith,anvil,Charlie,"Go to Blacksmith store")')
    action('Right click on Charlie to get choice bar')
    action('EnableInput()')
    choice2(charlie_earth)
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
    Message('Charlie: Hi! can I get this sword please')
    Message('Vendor: Sure! Have a good day!')
    action('Exit('+charlie_earth.name+',Blacksmith.Door')
    MysteryWorld(charlie_earth)

def AlchemyStore(charlie_earth):
    action('Enter('+charlie_earth.name+',AlchemyShop.Door)')
    Apple=Create_item('Apple','Apple','AlchemyShop.Table')
    EvilBook=Create_item('EvilBook','EvilBook','AlchemyShop.Bookshelf')
    Bag=Create_item('Bag','Bag','AlchemyShop.Bar')
    action('EnableIcon(buy_apple,apple,Charlie,"Buy apple")')
    action('EnableIcon(buy_bag,lockedchest,Charlie,"Buy Bag")')
    action('EnableIcon(buy_book,evilbook,Charlie,"Buy Book")')
    action('EnableInput()')
    choice3(charlie_earth)
    action('DisableInput()')

def buy_apple(charlie_earth):
    action('WalkTo('+charlie_earth.name+',Apple)')
    action('Take('+charlie_earth.name+',Apple)')
    action('WalkTo('+charlie_earth.name+', '+a_shop_vendor.name+')')
    action('Face('+a_shop_vendor.name+','+charlie_earth.name+')')
    Message('Charlie: Hi! can I get this apple')
    Message('Vendor: Sure! Have a good day!')
    action('Exit('+charlie_earth.name+',AlchemyShop.Door)')
    Message('Charlie goes back home after buying an apple and another boring day starts again!')
    action('SetPosition('+charlie_earth.name+',Cottage.Bed)')
    home(charlie_earth)

def buy_bag(charlie_earth):
    action('WalkTo('+charlie_earth.name+',Bag)')
    action('Take('+charlie_earth.name+',Bag)')
    action('WalkTo('+charlie_earth.name+', '+a_shop_vendor.name+')')
    action('Face('+a_shop_vendor.name+','+charlie_earth.name+')')
    Message('Charlie: Hi! can I get these this bag')
    Message('Vendor: Sure! Have a good day!')
    action('Exit('+charlie_earth.name+',AlchemyShop.Door)')
    Message('Charlie goes back home after buying a bag and another boring day starts again!')
    action('SetPosition('+charlie_earth.name+',Cottage.Bed)')
    home(charlie_earth)

def buy_book(charlie_earth):
    action('WalkTo('+charlie_earth.name+',EvilBook)')
    action('Take('+charlie_earth.name+',EvilBook)')
    action('WalkTo('+charlie_earth.name+', '+a_shop_vendor.name+')')
    action('Face('+a_shop_vendor.name+','+charlie_earth.name+')')
    Message('Charlie: Hi! can I get these two items please')
    Message('Vendor: Sure! Have a good day!')
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
    action('SetPosition('+charlie_earth.name+',P_MysteryWorld.NorthEnd)')
    action('CreateEffect('+charlie_earth.name+',Resurrection)')

    action('EnableIcon(Explore_city,city,Charlie,"Explore city")')
    action('EnableIcon(Fruit_shop,apple,Charlie,"Go to fruit shop")')
    action('EnableInput()')
    choice4(charlie_earth)
    action('DisableInput()')

def choice4(charlie_earth):
    while True:
        received=input()
        if received=='input Explore_city Charlie':
           return explore_city(charlie_earth)
        elif received=='input Fruit_shop Charlie':
           return visit_Fruitshop(charlie_earth)

def explore_city(charlie_earth):
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.WestEnd)')
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.Fountain)')
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.EastEnd)')
    action('Attack('+bandit1.name+','+charlie_earth.name+',False)')
    action('Attack('+bandit2.name+','+charlie_earth.name+',False)')

    action('EnableIcon(call_for_help,kneel,Charlie,"Call for help")')
    action('EnableIcon(engage_fight,fist,Charlie,"Engage fight")')
    action('EnableInput()')
    choice5(charlie_earth)
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
        find_dager(charlie_earth)
    elif charlie_earth.item=='dagger':
        Message('Since I have the dagger I have to find the Evil book')
        find_book(charlie_earth)

def find_book(charlie_earth):
    Message('Since you have a daggger find the book and use the spell to activate sword power')
    action('Enter('+charlie_earth.name+',AlchemyShop.Door)')
    EvilBook2=Create_item('EvilBook2','EvilBook','AlchemyShop.Bookshelf')
    action('WalkTo('+charlie_earth.name+',EvilBook2)')
    action('Take('+charlie_earth.name+',EvilBook2)')
    Message('Charlie reads the spell: Abrakha Dhabra Boom.')
    action('SetPosition(Sword_b,'+charlie_earth.name+')',False)
    action('EnableEffect(Spiralflame,Sword_b)')
    action('Exit('+charlie_earth.name+',AlchemyShop.Door')
    the_end(charlie_earth)

def visit_Fruitshop(charlie_earth):
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.RedHouseDoor)')
    action('Enter('+charlie_earth.name+',FruitShop.Door)')
    f_shop_vendor.give_item('Sword_t','Sword')
    action('Take('+charlie_earth.name+',Apple1_fruit)')
    action('WalkTo('+charlie_earth.name+','+f_shop_vendor.name+')')
    Message('Charlie: Hi! can I get this apple please)')
    Message('Vendor: Nahi!')
    Message('Charlie: Pardon me! I did not understand.')
    Message('Vendor: Yaha se baahar jaao, kon aadmi ho tum')
    Message('Things get esculated and the vendor gets angry!')
    f_shop_vendor.expression('angry')
    action('Draw('+f_shop_vendor.name+',Sword_t')
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