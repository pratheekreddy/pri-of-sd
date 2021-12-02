from action import action

def explore_city(charlie_earth,bandit1,bandit2,bandit3):
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.Horse)')
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.WestEnd)')
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.Fountain)')
    action('WalkTo('+charlie_earth.name+',P_MysteryWorld.EastEnd)')
    action('Attack('+bandit1.name+','+charlie_earth.name+',False)')
    action('Attack('+bandit2.name+','+charlie_earth.name+',False)')
    action('MoveAway('+charlie_earth.name+')')

