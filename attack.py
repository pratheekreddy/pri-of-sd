from action import action

def attack(x,y):
    action('WalkTo('+x+','+y+')',False)
    action('Face('+x+','+y+')')
    action('PlaySound(Draw)',False)
    action('Attack('+x+','+y+')',False)
    action('Die('+y+')')
