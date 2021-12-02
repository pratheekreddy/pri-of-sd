from action import action


def MysteryWorld(charlie_earth):
    action('SetPosition('+charlie_earth.name+',P_MysteryWorld.NorthEnd)')
    action('CreateEffect('+charlie_earth.name+',Resurrection)')