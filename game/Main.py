"""Learning everything python and this time about inheritance"""

from Zombie import *
from Ogre import *


def battle(e: Enemy):
    e.talk()
    e.attack()


zombie = Zombie(15, 2)
ogre = Ogre(20, 2)

battle(zombie)
battle(ogre)
