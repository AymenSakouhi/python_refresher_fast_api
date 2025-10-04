from Enemy import *


dragon = Enemy("Dragon", 15, 2)

dragon.talk()
dragon.walk_forward()
dragon.attack()

print(
    f"{dragon.type_of_enemy} has {dragon.health_points} health and can do an attack of {dragon.attack_damage}"
)
