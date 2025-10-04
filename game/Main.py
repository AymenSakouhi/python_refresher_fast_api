"""Learning everything python and this time about inheritance"""

from Zombie import *
from Ogre import *


zombie = Zombie(15, 2)
ogre = Ogre(20, 2)

zombie.talk()
zombie.walk_forward()
zombie.attack()
zombie.spead_disease()

ogre.talk()
ogre.charge()
