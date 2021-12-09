from action import action
from attack import attack
from find_book import find_book
from find_dager import find_dager
from message import Message, Message1, d_box
from start import emily,bandit1,bandit2,bandit3

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
    









