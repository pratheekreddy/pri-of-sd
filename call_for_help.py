from attack import attack
from message import Message

def call_for_help(emily,bandit1,bandit2,bandit3,charlie_earth):
    Message('Charlie: HELP!! HELP!! HELP!!')

    attack(emily.name,bandit1.name)
    attack(emily.name,bandit2.name)
    attack(emily.name,bandit3.name)

    Message('Charlie: Thank you soo much for rescuing me!. You are my hero!')
    Message('Emily: I am Emily!')
    Message('Charlie: I am Charlie!')
    Message('Emily: Are you new here?')
    Message('Charlie: Yes I am lost. I dont know how i got here.')
    Message('Emily: Thats weird! You are not from this world. I guess this happened to you because of the witch.')
    Message('Charlie: OMG! What should I do now?')
    Message('Emily: We have to find the witch and kill her with the dagger.')









