from Enemy import *


def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()
    while e1.health_points > 0 and e2.health_points > 0:
        e1.specia_attack()
        e2.specia_attack()
        e1.attack()
        e2.health_points -= e1.attack_damage
        print(f"{e2.get_type_of_enemy()} have {e2.health_points} left!")
        e2.attack()
        e1.health_points -= e2.attack_damage
        print(f"{e1.get_type_of_enemy()} have {e1.health_points} left!")

    if e2.health_points > 0:
        print(f"{e2.get_type_of_enemy()} wins")
    else:
        print(f"{e1.get_type_of_enemy()} wins")
