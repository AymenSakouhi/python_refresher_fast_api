from Enemy import *


class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(
            type_of_enemy="Zombie",
            health_points=health_points,
            attack_damage=attack_damage,
        )

    def talk(self):
        """Talking"""
        print(f"Grambliiiing")

    def spead_disease(self):
        """spreading infection"""
        print("Spreading infection")
