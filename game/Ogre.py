from Enemy import *


class Ogre(Enemy):
    def __init__(self, health_points, attack_damage) -> None:
        super().__init__(
            type_of_enemy="Ogre",
            health_points=health_points,
            attack_damage=attack_damage,
        )

    def talk(self):
        print("Arguing with hands")

    def charge(self):
        """charging at you with full speed"""
        print("charging at you")
