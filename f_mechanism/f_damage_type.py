def f_double_attack(d):
    d.f_stamina()
    damage = d.damage*2
    return damage


def f_tripple_attack(d):
    d.f_stamina()
    damage = d.damage*3
    return damage


def f_kill_shot(d):
    d.f_stamina()
    d.damage = d.health
    return d.damage
