from Enemy import *


enemy = Enemy()
enemy.type_of_enemy = "Zombie"

enemy.talk()
enemy.walk_forward()
enemy.attack()

print(
    f"{enemy.type_of_enemy} has {enemy.health_points} health and can do an attack of {enemy.attack_damage}"
)
