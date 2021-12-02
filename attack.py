from action import action

def attack(x,y):
    action('WalkTo('+x+','+y+')')
    action('Face('+x+','+y+')')
    action('PlaySound(Draw)',False)
    action('Attack('+x+','+y+')')
    action('Die('+y+')')
