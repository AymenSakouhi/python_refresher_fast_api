"""Learning everything python and this time about inheritance"""

from Zombie import *
from Ogre import *
from Hero import *
from Weapon import *
from Battle import battle, hero_battle


zombie = Zombie(10, 1)
ogre = Ogre(15, 2)
hero = Hero(20, 1)
weapon = Weapon("sword", 5)
hero.weapon = weapon
hero.equip_weapon()

# battle(zombie, ogre)
hero_battle(hero, ogre)
