import random
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

    def specia_attack(self):
        """generating health again"""
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            print("generating health, +2HP for zombie")
            self.health_points += 2
