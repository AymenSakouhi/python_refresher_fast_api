from Enemy import *
from Hero import *


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
    print("-----------")
    if e2.health_points > 0:
        print(f"{e2.get_type_of_enemy()} wins")
    else:
        print(f"{e1.get_type_of_enemy()} wins")


def hero_battle(hero: Hero, e: Enemy):
    hero.talk()
    e.talk()
    while hero.health_points > 0 and e.health_points > 0:
        e.specia_attack()
        e.attack()
        hero.health_points -= e.attack_damage
        print(f"hero have {hero.health_points} left!")
        hero.attack()
        e.health_points -= hero.attack_damage
        print(f"{e.get_type_of_enemy()} have {e.health_points} left!")
    print("-----------")
    if hero.health_points > 0:
        print(f"Hero wins")
    else:
        print(f"{e.get_type_of_enemy()} wins")
