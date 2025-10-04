"""Learning everything python and this time about inheritance"""

from Zombie import *
from Ogre import *
from Battle import battle


zombie = Zombie(10, 1)
ogre = Ogre(15, 2)

battle(zombie, ogre)
