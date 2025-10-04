from Enemy import *


dragon = Enemy("Dragon", 15, 2)

dragon.talk()
dragon.walk_forward()
dragon.attack()

print(dragon.get_type_of_enemy())
